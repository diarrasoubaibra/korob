from product.models.product_model import ProductModel
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['name_product', 'name_product', 'description_product','price', 'image']
