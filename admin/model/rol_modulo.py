
from django.db.models import Model
from django.db import models
from ..model.rol import rol_model
from ..model.usuario import usuario_model
from ..model.submodulo import submodulo_model

class rol_modulo_model(Model):
    id=models.AutoField(primary_key=True)
    roles=models.ForeignKey(rol_model,db_column='id_rol')
    modulos=models.ForeignKey(submodulo_model,db_column='id_modulo')
    id_usuario=models.IntegerField
    id_rol=models.IntegerField
    create=models.SmallIntegerField(default=0)
    pdf=models.SmallIntegerField(default=0)
    update=models.SmallIntegerField(default=0)
    excel=models.SmallIntegerField(default=0)
    delete=models.SmallIntegerField(default=0)
    assign=models.SmallIntegerField(default=0)
    class Meta:
        db_table='roles_modulos'
