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



class PartidoPolitico(models.Model):
    nombre = models.CharField(max_length=150)
    fundacion_anio = models.IntegerField()
    ruta_archivo = models.CharField(max_length=500)
    fecha_registro = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(null=True)

    class Meta:
        db_table = "organizacion_politica"
    def __str__(self):
        return self.organizacion_politica

