from rest_framework import serializers

from .models import Proceso, Cargo, OrganizacionPolitica, IndicadorCategoriaOrganizacion ,IndicadorCategoria

class ProcesoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proceso
        fields = ('nombre', 'estado')


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = ('cargo', 'estado')



class IndicadorCategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndicadorCategoria
        fields = ('indicador','nombre','alerta','estado','order','fecha_registro','fecha_modificacion')



class IndicadorCategoriaOrganizacionSerializer(serializers.ModelSerializer):

    indicadorescategoria = IndicadorCategoriaSerializer(many=True, read_only=True)
    class Meta:
        model = IndicadorCategoriaOrganizacion
        fields = ('indicador','indicador_categoria','organizacion','cantidad','porcentaje','alerta','estado','fecha_registro','fecha_modificacion','indicadorescategoria')


class OrganizacionPoliticaSerializer(serializers.ModelSerializer):

    # tracks = serializers.StringRelatedField(many=True)
    indicadorescategoriaorg = IndicadorCategoriaOrganizacionSerializer(many=True, read_only=True)
    class Meta:
        model = OrganizacionPolitica
        fields = ('nombre','fundacion_anio', 'estado','descripcion','ruta_archivo','jne_idorganizacionpolitica','fecha_registro','fecha_modificacion','indicadorescategoriaorg')

