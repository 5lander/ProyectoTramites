from rest_framework import serializers
from .models import Tramite

class TramiteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tramite
        fields= '__all__'



