from rest_framework import viewsets
from carts.models.cartsItem_models import CartsItemModel
from api.serializers.cartItem_serializer import CartsItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartsItemModel.objects.all()
    serializer_class = CartsItemSerializer
