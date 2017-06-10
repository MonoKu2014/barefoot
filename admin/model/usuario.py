__author__ = 'victorfx'

from django.db import models
from .rol import rol_model
from .pais import pais_model

class usuario_model(models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    usuario=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    fecha_creacion=models.DateTimeField
    fecha_actualizacion=models.DateTimeField
    email=models.CharField(max_length=50)
    codigo_password=models.CharField(max_length=250)
    rol=models.ForeignKey(rol_model,db_column='id_rol')
    pais=models.ForeignKey(pais_model,db_column='id_pais')
    id_rol=models.IntegerField
    ing_precio_dia=models.IntegerField()
    paises = models.ManyToManyField(pais_model, through='usuarios_paises_model')
    class Meta:
        db_table='usuarios'



class usuarios_paises_model(models.Model):
    id=models.AutoField(primary_key=True)
    usuarios=models.ForeignKey(usuario_model,db_column='usuario_id')
    paises=models.ForeignKey(pais_model,db_column='pais_id')
    class Meta:
        db_table='usuarios_paises'
