from rest_framework import viewsets
from carts.models.cart_model import CartModel
from api.serializers.cart_serializer import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
