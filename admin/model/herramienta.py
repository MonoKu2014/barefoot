from django.db import models
from .componente import componente_model

class herramienta_model(models.Model):
    HR_ID=models.AutoField(primary_key=True)
    HR_NOMBRE=models.CharField(max_length=50)
    componente=models.ForeignKey(componente_model,db_column='CO_ID',to_field='CO_ID')
    class Meta:
        db_table='herramienta'