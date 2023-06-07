from rest_framework.viewsets import ModelViewSet
from .models import Category, Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CategorySerializer, OrderSerializer
from .permissions import IsCurier, IsOwnerPersmission



class PermissionMixin:
    def get_permission(self):
        if self.action in ['create']:
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser, IsOwnerPersmission]
        elif self.action in ['get']:
            permissions = [IsCurier, IsAdminUser]



class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]



class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    serializer_classes = [PermissionMixin]
