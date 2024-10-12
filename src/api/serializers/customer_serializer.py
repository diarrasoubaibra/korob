from customer.models.customer_model import CustomerModel
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['id', 'username', 'number', 'password']
