from django.db import models
from .tipoc import tipoc_model
from .proveedor import proveedor_model
from .marca import marca_model

class componente_model(models.Model):
    CO_ID=models.AutoField(primary_key=True)
    CO_NOMBRE=models.CharField(max_length=50)
    CO_PRECIO=models.DecimalField()
    tipoc=models.ForeignKey(tipoc_model,db_column='TC_ID',to_field='TC_ID')
    proveedor=models.ForeignKey(proveedor_model,db_column='PV_RUT',to_field='PV_RUT')
    marca=models.ForeignKey(marca_model,db_column='CO_MARCA_ID',to_field='id')
    class Meta:
        db_table='componente'
