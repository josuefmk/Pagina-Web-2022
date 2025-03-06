from rest_framework import serializers
from suscripciones.models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['idservicio','nombreservicio','precio']