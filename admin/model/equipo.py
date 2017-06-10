from django.db import models
from .tipoe import tipoe_model
from .componente import componente_model


class equipo_model(models.Model):
    EQ_ID=models.AutoField(primary_key=True)
    EQ_NOMBRE=models.CharField(max_length=50)
    EQ_PRECIO=models.DecimalField()
    EQ_ESTADO=models.DecimalField()
    EQ_DOC_CONTRATO=models.CharField(max_length=500)
    tipoe=models.ForeignKey(tipoe_model,db_column='TE_ID',to_field='TE_ID')
    comunidades=models.ManyToManyField('comunidad_model',through='equipo_comunidades_model')
    class Meta:
        db_table='equipo'

