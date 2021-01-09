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

class Indicador(models.Model):
    nombre = models.CharField(max_length=150)
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


class Ubigeo(models.Model):
    ubigeo = models.CharField(max_length=10, primary_key=True)
    region = models.CharField(max_length=150)
    distrito_electoral = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "ubigeo"