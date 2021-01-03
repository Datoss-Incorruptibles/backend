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
    fundacion_anio = models.IntegerField()
    estado =  models.IntegerField()
    descripcion = models.CharField(max_length=500)
    ruta_archivo = models.CharField(max_length=500)
    jne_idorganizacionpolitica = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "organizacion_politica"
    def __str__(self):
        return self.organizacion_politica

class Indicador(models.Model):
    nombre = models.CharField(max_length=150)
    alerta = models.IntegerField()
    estado = models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "_indicador"
    def __str__(self):
        return self._indicador


class IndicadorCategoria(models.Model):
    indicador_id = models.IntegerField()
    nombre = models.CharField(max_length=150)
    alerta = models.IntegerField()
    estado =  models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "_indicador_categoria"
    def __str__(self):
        return self._indicador_categoria



class IndicadorCategoriaOrganizacion(models.Model):
    indicador_id = models.IntegerField()
    indicador_categoria_id = models.IntegerField()
    organizacion_id  = models.IntegerField()
    cantidad =  models.IntegerField()
    porcentaje  = models.FloatField()
    alerta =  models.IntegerField()
    estado =  models.IntegerField()
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)
    class Meta:
        db_table = "_indicador_categoria_organizacion"
    def __str__(self):
        return self._indicador_categoria_organizacion
