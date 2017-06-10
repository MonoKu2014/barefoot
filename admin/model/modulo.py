__author__ = 'victorfx'

from django.db import models
from rest_framework import serializers

class modulo_model(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    fecha_creacion=models.DateTimeField
    fecha_actualizacion=models.DateTimeField
    class Meta:
        db_table='modulos'

class serializer(serializers.Serializer):
    id=serializers.IntegerField
    nombre=serializers.CharField
    fecha_creacion=serializers.DateTimeField
    fecha_actualizacion=serializers.DateTimeField