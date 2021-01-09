from rest_framework import serializers

from .models import Proceso, Cargo, OrganizacionPolitica, \
IndicadorCategoriaOrganizacion ,IndicadorCategoria, Indicador, \
Ubigeo

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
class IndicadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicador
        fields = ('nombre','alerta','estado')
class IndicadorCategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndicadorCategoria
        fields = ('indicador','nombre','alerta','estado','order')

class IndicadorCategoriaOrganizacionSerializer(serializers.ModelSerializer):
    indicador_categoria_nombre = serializers.CharField(source='indicador_categoria', read_only=True)
    indicador_nombre = serializers.CharField(source='indicador', read_only=True)
    class Meta:
        model = IndicadorCategoriaOrganizacion
        fields = ('indicador_categoria_nombre','indicador_categoria','indicador_nombre','indicador',
                'cantidad','porcentaje','alerta','estado')


class OrganizacionPoliticaSerializer(serializers.ModelSerializer):
    id = serializers
    # tracks = serializers.StringRelatedField(many=True)
    indicadorescategoriaorg = IndicadorCategoriaOrganizacionSerializer(many=True, read_only=True)
    class Meta:
        model = OrganizacionPolitica
        fields = ('id','nombre','fundacion_fecha', 'estado','descripcion','ruta_archivo','jne_idorganizacionpolitica','indicadorescategoriaorg')

