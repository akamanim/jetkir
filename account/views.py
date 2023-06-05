from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Succefully registered', 201)
        


class ActivationView(APIView):
    def get(self, request, phone_number, activation_code):
        user = User.objects.filter(phone_number=phone_number, activation_code=activation_code).first()
        if not user:
            return Response('user does not exists', 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', 200)