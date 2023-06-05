from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_lenght=4, required=True, write_only=True)
    password_confirm = serializers.CharField(min_lenght=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'password_confirm')

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        return attrs
    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # send_activation_code_celery.delay(user.email, user.activation_code)
        return user