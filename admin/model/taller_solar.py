from django.db import models
from ..model.comunidad import comunidad_model

class taller_solar_model(models.Model):

    TS_ID=models.AutoField(primary_key=True)
    TS_LUGAR=models.CharField(max_length=50)
    TS_DIAS_USO_INGENIEROS=models.IntegerField()
    TS_DIAS_USO_COMUNIDAD=models.IntegerField()
    TS_DESCRIPCION=models.CharField(max_length=99)
    TS_HABILITADO=models.DecimalField()
    comunidad=models.ForeignKey(comunidad_model,db_column='TS_CM_ID')

    class Meta:
        db_table='talleres_solares'