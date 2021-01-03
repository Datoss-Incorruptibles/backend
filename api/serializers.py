from rest_framework import serializers

from .models import Proceso, Cargo, PartidoPolitico

class ProcesoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proceso
        fields = ('nombre', 'estado')


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = ('cargo', 'estado')

class PartidoPoliticoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartidoPolitico
        fields = ('nombre', 'fundacion_anio','ruta_archivo')

