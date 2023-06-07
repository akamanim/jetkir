from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CategoryViewset

router = DefaultRouter()

router.register('orders', OrderViewSet)
router.register('category', CategoryViewset)

urlpatterns = [
    path('', include(router.urls))
]