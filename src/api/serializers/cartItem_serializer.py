from carts.models.cartsItem_models import CartsItemModel
from rest_framework import serializers

class CartsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartsItemModel
        fields = '__all__'
