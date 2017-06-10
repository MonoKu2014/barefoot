from django.db import models

class tipoc_model(models.Model):
    TC_ID=models.CharField(primary_key=True)
    TC_NOMBRE=models.CharField()
    class Meta:
        db_table='tipoc'