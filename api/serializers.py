from rest_framework import serializers

from .models import Proceso, Cargo, Ubigeo

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = ('nombre', 'estado')


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('cargo', 'estado')


class UbigeoSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='ubigeo', read_only=True)
    class Meta:
        model = Ubigeo
        fields = ('id','region','distrito_electoral')