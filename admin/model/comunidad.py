from django.db import models
from .pais import pais_model
from .equipo import equipo_model
from .tipoe import tipoe_model

class comunidad_model(models.Model):
    CM_ID=models.AutoField(primary_key=True)
    CM_NOMBRE=models.CharField(max_length=50)
    CM_PAIS=models.CharField(max_length=2)
    CM_NUMEQUIPOS=models.DecimalField()
    CM_CASAS=models.DecimalField()
    CM_TIENDAS=models.DecimalField()
    CM_EDIFICIOS=models.DecimalField()
    CM_FIRMADO=models.DecimalField()
    CM_RESERVADO=models.DecimalField()
    CM_PORCINST=models.DecimalField()
    CN_PERINIENT=models.DateField()
    CN_PERFINENT=models.DateField()
    CN_FECENT=models.DateField()
    CN_CAPACITA=models.DecimalField()
    CN_CANTCAP=models.DecimalField()
    CN_GENCAP=models.DecimalField()
    CM_DOC_DONACION_COMITE=models.CharField(max_length=500)
    CM_DOC_CMI=models.CharField(max_length=500)
    CM_DOC_CUENTA_BANCARIA=models.CharField(max_length=500)
    pais=models.ForeignKey(pais_model,db_column='PA_ID')
    equipos = models.ManyToManyField(equipo_model, through='equipo_comunidades_model')
    class Meta:
        db_table='comunidad'





class equipo_comunidades_model(models.Model):
    EQ_CM_ID=models.AutoField(primary_key=True)
    equipos=models.ForeignKey(equipo_model,db_column='EQ_ID')
    comunidades=models.ForeignKey(comunidad_model,db_column='CM_ID')
    class Meta:
        db_table='equipo_comunidades'




