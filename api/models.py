from django.db import models
from datetime import datetime 

class Proceso(models.Model):
    nombre = models.CharField(max_length=150)
    estado = models.IntegerField()
    jne_idproceso = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
 
    class Meta:
        db_table = "proceso"

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    cargo = models.CharField(max_length=150)
    estado = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "cargo"
    def __str__(self):
        return self.cargo

class OrganizacionPolitica(models.Model):
    nombre = models.CharField(max_length=150)
    fundacion_fecha = models.DateField(null=True)
    estado =  models.IntegerField()
    descripcion = models.TextField()
    ruta_archivo = models.CharField(max_length=500)
    jne_idorganizacionpolitica = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    url = models.CharField(max_length=150)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "organizacion_politica"
    def __str__(self):
        return self.nombre

    @property
    def sentencia_civil(self):
        return IndicadorCategoriaOrganizacion.objects.filter(indicador=8,organizacion=self.pk).count()

class Indicador(models.Model):
    nombre = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    ubicacion = models.IntegerField()
    alerta = models.IntegerField()
    estado = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "indicador"
    def __str__(self):
        return self.nombre


class IndicadorCategoria(models.Model):
    indicador = models.ForeignKey("Indicador", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    alerta = models.IntegerField()
    estado =  models.IntegerField()
    order  = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "indicador_categoria"
    def __str__(self):
        return self.nombre

class IndicadorCategoriaOrganizacion(models.Model):
    indicador = models.ForeignKey("Indicador", on_delete=models.CASCADE)
    indicador_categoria = models.ForeignKey("IndicadorCategoria", on_delete=models.CASCADE)
    organizacion  = models.ForeignKey("OrganizacionPolitica", related_name='indicadorescategoriaorg', on_delete=models.CASCADE)

    cantidad =  models.IntegerField()
    porcentaje  = models.FloatField()
    alerta =  models.IntegerField()
    estado =  models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "indicador_categoria_organizacion"
        ordering = ('indicador','indicador_categoria__order')

class IndicadorCategoriaCandidato(models.Model):
    indicador = models.ForeignKey("Indicador", on_delete=models.CASCADE)
    indicador_categoria = models.ForeignKey("IndicadorCategoria", on_delete=models.CASCADE)
    candidato  = models.ForeignKey("Candidato", related_name='indicadores_categoria_candidato', on_delete=models.CASCADE)

    cantidad =  models.IntegerField()
    porcentaje  = models.FloatField()
    alerta =  models.IntegerField()
    estado =  models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "indicador_categoria_candidato"
        ordering = ('indicador','indicador_categoria__order')


class Candidato(models.Model):

    jne_idcandidato = models.IntegerField()
    jne_idhojavida = models.IntegerField()
    jne_estado_lista =  models.CharField(max_length=150)
    jne_estado_expediente =  models.CharField(max_length=150)
    jne_estado_hojavida =  models.CharField(max_length=150)
    jne_posicion =  models.IntegerField()
    jne_organizacion_politica =  models.CharField(max_length=150)
    cargo_id =  models.IntegerField()
    proceso_id =  models.IntegerField()
    organizacion_politica_id =  models.IntegerField()
    documento_identidad =  models.CharField(max_length=150)
    apellido_paterno =  models.CharField(max_length=150)
    apellido_materno =  models.CharField(max_length=150)
    nombres =  models.CharField(max_length=150)
    fecha_nacimiento =  models.DateField()
    profesion =  models.CharField(max_length=500, null=True)
    nivel_estudio_id_max =  models.IntegerField(null=True)
    region =  models.CharField(max_length=150, null=True)
    distrito_electoral =  models.CharField(max_length=150, null=True)
    ubigeo_postula =  models.CharField(max_length=150, null=True)
    ruta_archivo =  models.CharField(max_length=150, null=True)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "candidato"

    @property
    def organizacion_politica_logo(self):
        return OrganizacionPolitica.objects.get(pk=self.organizacion_politica_id).ruta_archivo

class Ubigeo(models.Model):
    ubigeo = models.CharField(max_length=10, primary_key=True)
    region = models.CharField(max_length=150)
    distrito_electoral = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "ubigeo"


class CandidatoEstudio(models.Model):

    jne_idhojavida = models.IntegerField()
    jne_idhvestudio = models.IntegerField()
    jne_tabla = models.CharField(max_length=150)  	
    nivel_estudio_id = models.CharField(max_length=250) 
    nivel_estudio = models.CharField(max_length=250)
    nivel_estudio_estado = models.CharField(max_length=250)
    grado = models.CharField(max_length=250)
    institucion = models.CharField(max_length=250)
    estudio = models.CharField(max_length=250)
    institucion_id = models.IntegerField()
    estudio_id = models.IntegerField()
    comentario = models.TextField(null=True)
    anio_bachiller = models.CharField(max_length=4)
    anio_titulo = models.CharField(max_length=4)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "candidato_estudio"


class CandidatoJudicial(models.Model):

    sentencia = models.CharField(max_length=150)
    nro_expediente = models.CharField(max_length=50)
    fallo = models.CharField(max_length=500)
    cumple_fallo = models.CharField(max_length=150, null=True)
    fecha_sentencia = models.DateField(null=True)
    modalidad = models.CharField(max_length=150, null=True)
    tipo_proceso = models.CharField(max_length=150)
    estado_proceso = models.CharField(max_length=50)
    jne_idhojavida = models.IntegerField()
    jne_idhvsentencia = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "candidato_judicial"


class CandidatoExperiencia(models.Model):

    tipo = models.IntegerField()
    jne_idhojavida = models.IntegerField()
    jne_idhvexpelaboral = models.IntegerField()	
    item_expelaboral = models.IntegerField()
    centro_trabajo = models.CharField(max_length=250)
    ocupacion_profesion = models.CharField(max_length=250)
    anio_trabajo_desde = models.CharField(max_length=4)
    anio_trabajo_hasta = models.CharField(max_length=4)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "candidato_experiencia"



class CandidatoIngreso(models.Model):
    jne_idhojavida = models.IntegerField()
    jne_idhvingresos = models.IntegerField()
    renta_bruta_privado = models.DecimalField(max_digits=15, decimal_places=2)
    renta_bruta_publico = models.DecimalField(max_digits=15, decimal_places=2)
    renta_individual_privado = models.DecimalField(max_digits=15, decimal_places=2)
    renta_individual_publico = models.DecimalField(max_digits=15, decimal_places=2)
    otros_ingresos_privado = models.DecimalField(max_digits=15, decimal_places=2)
    otros_ingresos_publico = models.DecimalField(max_digits=15, decimal_places=2)
    anio_ingresos = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = 'candidato_ingreso'
        verbose_name='Candidato Ingresos'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.id

class CandidatoInmueble(models.Model):

    jne_idhojavida = models.IntegerField()
    jne_idhvbieninmueble = models.IntegerField()
    jne_strinmueblesunarp = models.IntegerField() 
    jne_decautovaluo = models.FloatField()
    direccion = models.TextField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    order = models.IntegerField()
    comentario = models.TextField(null=True)
    partida_sunarp = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=80)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'candidato_inmueble'
        verbose_name='Candidato Bienes Inmuebles'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.partida_sunarp


class CandidatoMueble(models.Model):
    jne_idhojavida = models.IntegerField()
    jne_idhvbienmueble = models.IntegerField()
    caracteristica = models.CharField(max_length=100)
    comentario = models.CharField(max_length=250, null=True, blank=True)
    marca =  models.CharField(max_length=100, null=True, blank=True)
    order = models.IntegerField()
    modelo = models.CharField(max_length=100, null=True, blank=True)
    placa = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    vehiculo = models.CharField(max_length=100)

    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'candidato_mueble'
        verbose_name = "Candidato Bienes Muebles"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.vehiculo



class CandidatoMedio(models.Model):
    TIPO_NOTICIA = [
        ('video', 'Video'),
        ('web', 'Web'),
    ]
    jne_idhojavida = models.IntegerField()
    titulo = models.CharField(max_length=250)    
    url = models.URLField(max_length=250)
    tipo = models.CharField(max_length=10, choices=TIPO_NOTICIA, default='web')
    fecha = models.DateField()
    medio = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    imagen = models.CharField(max_length=250, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = 'candidato_medio'
        verbose_name = "Candidato Medios"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.titulo

class PlanCriterio(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=30)
    peso = models.IntegerField(null=True)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = 'plan_criterio'
        verbose_name = "Plan criterio"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nombre


class OrganizacionPlan(models.Model):    
    jne_idplangobierno = models.IntegerField()
    tipo_eleccion = models.IntegerField()
    organizacion_politica = models.ForeignKey("OrganizacionPolitica", related_name='planes', on_delete=models.CASCADE)
    ruta_archivo = models.CharField(max_length=250)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'organizacion_plan'
        verbose_name = "Organizacion Plan"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ruta_archivo

    @property
    def tipo_plan(self):
        TIPO_PLAN = {1: 'Plan presidencial', 3: 'Plan parlamento andino'}
        return TIPO_PLAN[self.tipo_eleccion]


class OrganizacionPlanDetalle(models.Model):
    plan = models.ForeignKey("OrganizacionPlan", related_name='plan_detalles', on_delete=models.CASCADE)
    jne_idplangobierno = models.IntegerField()
    jne_idplangobdimension = models.IntegerField()
    problema = models.CharField(max_length=300)
    objetivo = models.CharField(max_length=300)
    meta = models.CharField(max_length=300)
    indicador = models.CharField(max_length=300)
    dimension_id = models.IntegerField()
    plan_criterio = models.ForeignKey("PlanCriterio", related_name='plan_detalles', on_delete=models.CASCADE)
    valor = models.IntegerField(null=True)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = 'organizacion_plan_detalle'
        verbose_name = "Organizacion Plan detalle"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.problema

class OrganizacionPlanCriterio(models.Model):
    jne_idplangobierno = models.IntegerField()
    plan_criterio_id = models.IntegerField()
    puntaje = models.FloatField(null=True)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = 'organizacion_plan_criterio'
        verbose_name = "Organizacion Plan criterio"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pk
