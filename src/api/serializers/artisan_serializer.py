from rest_framework import serializers
from artisan.models.artisan_model import ArtisanModel

class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtisanModel
        fields = ['id', 'username', 'work', 'sex', 'number', 'whatsapp_number', 'pseudo', 'picture', 'password']


