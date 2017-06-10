from django.db import models

class marca_model(models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    class Meta:
        db_table='marcas'