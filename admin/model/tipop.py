from django.db import models
from .equipocom import equipocom_model

class tipop_model(models.Model):
    TP_ID=models.CharField(primary_key=True)
    EC_ID=models.CharField()
    TP_NOMBRE=models.CharField()
    equipocom=models.ForeignKey(equipocom_model,db_column='EC_ID',to_field='EC_ID')
    class Meta:
        db_table='tipop'