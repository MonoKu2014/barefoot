from django.db import models

class proveedor_model(models.Model):
    PV_ID=models.AutoField(primary_key=True)
    PV_RUT=models.CharField(max_length=15)
    PV_NOMBRE=models.CharField(max_length=50)
    PV_DIRECCION=models.CharField(max_length=80)
    PV_FONO=models.CharField(max_length=20)
    PV_MAIL=models.CharField(max_length=50)
    PV_FECHA=models.DateField(max_length=50)
    PV_VENTA=models.DecimalField()
    class Meta:
        db_table='proveedor'