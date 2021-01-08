from rest_framework import serializers

from .models import Proceso, Cargo, OrganizacionPolitica, IndicadorCategoriaOrganizacion, IndicadorCategoriaCandidato ,IndicadorCategoria, Indicador ,Candidato

class ProcesoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proceso
        fields = ('nombre', 'estado')


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = ('cargo', 'estado')


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

class IndicadorCategoriaCandidatoSerializer(serializers.ModelSerializer):
    indicador_categoria_nombre = serializers.CharField(source='indicador_categoria', read_only=True)
    indicador_nombre = serializers.CharField(source='indicador', read_only=True)
    class Meta:
        model = IndicadorCategoriaCandidato
        fields = ('indicador_categoria_nombre','indicador_categoria','indicador_nombre','indicador',
                'cantidad','porcentaje','alerta','estado')


class OrganizacionPoliticaSerializer(serializers.ModelSerializer):
    id = serializers
    # tracks = serializers.StringRelatedField(many=True)
    indicadorescategoriaorg = IndicadorCategoriaOrganizacionSerializer(many=True, read_only=True)
    class Meta:
        model = OrganizacionPolitica
        fields = ('id','nombre','fundacion_anio', 'estado','descripcion','ruta_archivo','jne_idorganizacionpolitica','indicadorescategoriaorg')


class CandidatoSerializer(serializers.ModelSerializer):
    id = serializers

    # candidatos by org pol and cargo pol 
    indicadores_categoria_candidato = IndicadorCategoriaCandidatoSerializer(many=True, read_only=True)

    class Meta:
        model = Candidato
        fields = ('id', 'jne_idcandidato','jne_idhojavida','jne_estado_lista', 'jne_estado_expediente','jne_estado_hojavida','jne_posicion','jne_organizacion_politica','cargo_id',
        'proceso_id','proceso_id','organizacion_politica_id', 'documento_identidad','apellido_paterno','apellido_materno','nombres',
        'profesion','nivel_estudio_id_max','region', 'distrito_electoral','ubigeo_postula','ruta_archivo','fecha_registro','fecha_modificacion','indicadores_categoria_candidato')

