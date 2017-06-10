from django.db import models
from ..model.modulo import modulo_model

class submodulo_model(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    modulo=models.ForeignKey(modulo_model,db_column='modulo_id')
    class Meta:
        db_table='submodulos'
