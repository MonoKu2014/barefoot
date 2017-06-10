from django.db import models
from .equipo import equipo_model
from .componente import componente_model


class equipocom_model(models.Model):
    EC_ID=models.AutoField(primary_key=True)
    EC_REVISION=models.DecimalField()
    EC_ESTADO=models.DecimalField()
    EC_PROBLEMA=models.CharField()
    EC_REPUESTO=models.DecimalField()
    EC_HERRAMIENTA=models.DecimalField()
    EC_HERRNOTA=models.CharField()
    EC_REPUESTO_ASIGNADO=models.IntegerField(default=0)
    equipo=models.ForeignKey(equipo_model,db_column='EQ_ID',to_field='EQ_ID')
    componente=models.ForeignKey(componente_model,db_column='CO_ID',to_field='CO_ID')
    class Meta:
        db_table='equipocom'