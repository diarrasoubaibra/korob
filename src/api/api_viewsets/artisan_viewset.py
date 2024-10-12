from rest_framework import viewsets
from artisan.models.artisan_model import ArtisanModel
from api.serializers.artisan_serializer import ArtisanSerializer

class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = ArtisanModel.objects.all()
    serializer_class = ArtisanSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password', None) 
        artisan = serializer.save() 
        if password:
            artisan.set_password(password)  
            artisan.save()

    def perform_update(self, serializer):
        """Surcharge de la méthode update pour gérer la mise à jour du mot de passe"""
        password = serializer.validated_data.pop('password', None)
        artisan = serializer.save() 
        if password:
            artisan.set_password(password) 
            artisan.save()
