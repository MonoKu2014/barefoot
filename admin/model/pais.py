from django.db import models

class pais_model(models.Model):

    PA_ID=models.AutoField(primary_key=True)
    PA_NOMBRE=models.CharField(max_length=50)
    class Meta:
        db_table='pais'