from rest_framework import serializers

from .models import Proceso, Cargo, OrganizacionPolitica, \
IndicadorCategoriaOrganizacion, IndicadorCategoria, Indicador, \
IndicadorCategoriaCandidato, Ubigeo, Candidato, CandidatoEstudio, \
CandidatoJudicial, CandidatoExperiencia, IndicadorCategoriaCandidato, \
CandidatoIngreso, CandidatoInmueble, CandidatoMueble

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



class OrgPolComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizacionPolitica
        fields = ('id','nombre', 'estado','jne_idorganizacionpolitica')


        
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
    indicador_titulo = serializers.CharField(source='indicador.titulo', read_only=True)
    indicador_ubicacion = serializers.IntegerField(source='indicador.ubicacion', read_only=True)
    indicador_alerta = serializers.IntegerField(source='indicador.alerta', read_only=True)

    class Meta:
        model = IndicadorCategoriaOrganizacion
        fields = ('indicador_categoria_nombre','indicador_categoria','indicador',
                'cantidad','porcentaje','alerta','indicador_titulo','indicador_ubicacion','indicador_alerta')

class IndicadorCategoriaCandidatoSerializer(serializers.ModelSerializer):
    indicador_categoria_nombre = serializers.CharField(source='indicador_categoria', read_only=True)
    indicador_nombre = serializers.CharField(source='indicador', read_only=True)
    class Meta:
        model = IndicadorCategoriaCandidato
        fields = ('indicador_categoria_nombre','indicador_categoria','indicador_nombre','indicador',
                'cantidad','porcentaje','alerta','estado')


class OrganizacionPoliticaSerializer(serializers.ModelSerializer):
    indicadorescategoriaorg = IndicadorCategoriaOrganizacionSerializer(many=True, read_only=True)
    sentencias = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrganizacionPolitica
        fields = ('id','nombre','fundacion_fecha', 'estado','descripcion','ruta_archivo',
                    'jne_idorganizacionpolitica','indicadorescategoriaorg','sentencias')


class CandidatoSerializer(serializers.ModelSerializer):

    # candidatos by org pol and cargo pol 
    indicadores = serializers.SerializerMethodField()

    def get_indicadores(self, obj):
        indicadores = IndicadorCategoriaCandidato.objects.filter(candidato=obj.pk, estado=1).order_by('indicador','indicador_categoria')
        if not indicadores:
            return None
        return IndicadoresCandidatoSerializer(indicadores, many=True, read_only=True).data

    class Meta:
        model = Candidato
        fields = ('id', 'jne_idcandidato','jne_idhojavida','jne_estado_lista', 'jne_estado_expediente','jne_estado_hojavida','jne_posicion','jne_organizacion_politica','cargo_id',
        'proceso_id','proceso_id','organizacion_politica_id','organizacion_politica_logo', 'documento_identidad','apellido_paterno','apellido_materno','nombres',
        'profesion','nivel_estudio_id_max','region', 'distrito_electoral','ubigeo_postula','ruta_archivo','fecha_registro','fecha_modificacion','indicadores')


class IndicadoresCandidatoSerializer(serializers.Serializer):

    indicador_categoria = serializers.CharField(source="indicador_categoria.nombre")
    indicador_categoria_id = serializers.IntegerField()
    indicador = serializers.CharField(source="indicador.titulo")
    indicador_id = serializers.IntegerField()
    cantidad = serializers.IntegerField()
    porcentaje = serializers.FloatField()
    alerta = serializers.IntegerField()
    estado = serializers.IntegerField()


class CandidatoDetailSerializer(serializers.ModelSerializer):
    indicadores_categoria_candidato = IndicadorCategoriaCandidatoSerializer(many=True, read_only=True)
    estudios = serializers.SerializerMethodField()
    sentencias = serializers.SerializerMethodField()
    experiencialaboral = serializers.SerializerMethodField()
    experienciapolitica = serializers.SerializerMethodField()
    ingresos = serializers.SerializerMethodField()

    def get_sentencias(self, obj):
        candidato_sentencias = CandidatoJudicial.objects.filter(jne_idhojavida=obj.jne_idhojavida).order_by('tipo_proceso')
        if not candidato_sentencias:
            return None
        return CandidatoJudicialSerializer(candidato_sentencias, many=True).data

    def get_estudios(self, obj):
        candidato_estudios = CandidatoEstudio.objects.filter(jne_idhojavida=obj.jne_idhojavida).order_by('-nivel_estudio_id')
        if not candidato_estudios:
            return None
        return CandidatoEstudioSerializer(candidato_estudios, many=True).data

    def get_experiencialaboral(self, obj):
        candidato_exp_laboral = CandidatoExperiencia.objects.filter(jne_idhojavida=obj.jne_idhojavida, tipo=1).order_by('-anio_trabajo_desde')
        if not candidato_exp_laboral:
            return None
        return CandidatoExperiencialSerializer(candidato_exp_laboral, many=True).data

    def get_experienciapolitica(self, obj):
        candidato_exp_politica = CandidatoExperiencia.objects.filter(jne_idhojavida=obj.jne_idhojavida, tipo=3).order_by('-anio_trabajo_desde')
        if not candidato_exp_politica:
            return None
        return CandidatoExperiencialSerializer(candidato_exp_politica, many=True).data

    def get_ingresos(self, obj):
        candidato_ingresos = CandidatoIngreso.objects.filter(jne_idhojavida=obj.jne_idhojavida)
        if not candidato_ingresos:
            return None
        return CandidatoIngresoSerializer(candidato_ingresos, many=True).data
       

    class Meta:
        model = Candidato
        fields = ('id', 'jne_idcandidato','jne_idhojavida','jne_estado_lista', 'jne_estado_expediente','jne_estado_hojavida','jne_posicion','jne_organizacion_politica','cargo_id',
                    'proceso_id','proceso_id','organizacion_politica_id','organizacion_politica_logo', 'documento_identidad','apellido_paterno','apellido_materno','nombres',
                    'profesion','nivel_estudio_id_max','region', 'distrito_electoral','ubigeo_postula','ruta_archivo','fecha_nacimiento','fecha_registro','fecha_modificacion',
                    'indicadores_categoria_candidato','sentencias','estudios','experiencialaboral','experienciapolitica','ingresos')




class CandidatoEstudioSerializer(serializers.Serializer):
    grado = serializers.CharField()
    institucion = serializers.CharField()
    estudio = serializers.CharField()
    anio_bachiller = serializers.CharField()
    anio_titulo = serializers.CharField()
    nivel_estudio_estado = serializers.CharField()

class CandidatoJudicialSerializer(serializers.Serializer):
    tipo_proceso = serializers.CharField()
    sentencia = serializers.CharField()
    nro_expediente = serializers.CharField()
    fallo = serializers.CharField()
    cumple_fallo = serializers.CharField()
    tipo_proceso = serializers.CharField()


class CandidatoExperiencialSerializer(serializers.Serializer):
    centro_trabajo = serializers.CharField()
    ocupacion_profesion = serializers.CharField()
    anio_trabajo_desde = serializers.CharField()
    anio_trabajo_hasta = serializers.CharField()


class CandidatoIngresoSerializer(serializers.Serializer):

    renta_bruta_privado = serializers.FloatField()
    renta_bruta_publico = serializers.FloatField()
    renta_individual_privado = serializers.FloatField()
    renta_individual_publico = serializers.FloatField()
    otros_ingresos_privado = serializers.FloatField()
    otros_ingresos_publico = serializers.FloatField()
    anio_ingresos = serializers.IntegerField()