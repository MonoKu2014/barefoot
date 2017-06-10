from django.db import models
from .pais import pais_model
from .usuario import usuario_model

class ingeniero_solar_model(models.Model):
    ING_ID=models.AutoField(primary_key=True)
    ING_PRECIO_DIA=models.IntegerField()
    ING_NOMBRE=models.CharField(max_length=50)
    pais=models.ForeignKey(pais_model,db_column='ING_PAIS_ID',to_field='PA_ID')
    usuario=models.ForeignKey(usuario_model,db_column='ING_USUARIO_ID',to_field='id')
    class Meta:
        db_table='ingenieros_solares'