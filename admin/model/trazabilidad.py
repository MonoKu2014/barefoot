from django.db import models
from .equipo import equipo_model

class trazabilidad_model(models.Model):
    TZ_ID=models.CharField(primary_key=True)
    EQ_ID=models.CharField()
    TRAZA2=models.CharField()
    TZ_FECHA=models.DateField()
    TRAZA4=models.CharField()
    TRAZA5=models.CharField()
    TRAZA6=models.CharField()
    TRAZA7=models.CharField()
    equipo=models.ForeignKey(equipo_model,db_column='EQ_ID',to_field='EQ_ID')
    class Meta:
        db_table='trazabilidad'
