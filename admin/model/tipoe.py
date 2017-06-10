from django.db import models

class tipoe_model(models.Model):
    TE_ID=models.CharField(primary_key=True)
    TE_NOMBRE=models.CharField()
    class Meta:
        db_table='tipoe'