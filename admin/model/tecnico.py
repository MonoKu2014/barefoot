from django.db import models
from .pais import pais_model

class tecnico_model(models.Model):

    TN_ID=models.CharField(primary_key=True)
    PA_ID=models.CharField()
    TN_NOMBRE=models.CharField()
    pais=pais=models.ForeignKey(pais_model,db_column='PA_ID',to_field='PA_ID')
    class Meta:
        db_table='tecnico'