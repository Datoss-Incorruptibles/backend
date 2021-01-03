from rest_framework import serializers

from .models import Proceso, Cargo

class ProcesoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proceso
        fields = ('nombre', 'estado')


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = ('cargo', 'estado')

