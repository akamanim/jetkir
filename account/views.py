from rest_framework.views import APIView

from .serializers import RegisterSerializer
from rest_framework.response import Response
from .models import User
from orders.permissions import IsCurier
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Successfully registerd', 201
            )


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response(
                'user does not exist', 400
            )
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response(
            'Activated', 200
        )


# class RegisterCurierView(APIView):
#     def post(self,email, surname, passport_image, techpassport_image, transport_image):
#         user = User.objects.filter(email=email)
#         user.surname = surname
#         user.passport_image = passport_image
#         user.techpassport_image = techpassport_image
#         user.transport_image = transport_image
#         return Response('Registered! Wait for responce', 200)
#     # permission_classes = [IsAuthenticated]


# class ActivateCurierView(APIView):
#     def post(self, email):
#         user = User.objects.filter(email=email)
#         user.is_curier = True
#         return Response('Activated', 200)
#     permission_classes = [IsCurier]

class RegisterCourierView(APIView):
    def post(self, request):
        email = request.data.get('email')
        surname = request.data.get('surname')
        passport_image = request.data.get('passport_image')
        techpassport_image = request.data.get('techpassport_image')
        transport_image = request.data.get('transport_image')

        user = User.objects.filter(email=email).first()
        if user:
            user.surname = surname
            user.passport_image = passport_image
            user.techpassport_image = techpassport_image
            user.transport_image = transport_image
            user.save()
            return Response('Registered! Wait for response', status=200)
        else:
            return Response('User not found', status=404)


class ActivateCourierView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        if user:
            user.is_curier = True
            user.save()
            return Response('Activated', status=200)
        else:
            return Response('User not found', status=404)
