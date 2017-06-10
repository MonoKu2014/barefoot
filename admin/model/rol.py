from django.db import models
from ..model.submodulo import submodulo_model

class rol_model(models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    ing_solar=models.IntegerField()
    fecha_creacion=models.DateTimeField
    fecha_actualizacion=models.DateTimeField
    submodulos= models.ManyToManyField(submodulo_model, through='roles_modulos_model')
    class Meta:
        db_table='roles'


class roles_modulos_model(models.Model):
    id=models.AutoField(primary_key=True)
    roles=models.ForeignKey(rol_model,db_column='id_rol')
    submodulos=models.ForeignKey(submodulo_model,db_column='id_modulo')
    class Meta:
        db_table='roles_modulos'

