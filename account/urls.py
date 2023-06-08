from django.urls import path
from .views import RegisterView, ActivationView, RegisterCourierView, ActivateCourierView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 




urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('curier/register/', RegisterCourierView.as_view()),
    path('curier/activate/', ActivateCourierView.as_view())
]

# urlpatterns = [
#     path('register/', RegisterView.as_view()),
#     path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh')]