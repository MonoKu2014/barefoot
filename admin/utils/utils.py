
import hashlib
import os
import datetime
from ..model.equipocom import equipocom_model

def ext_md5_file(nombre):
    filename = nombre
    ext = os.path.splitext(filename)[1]
    ext = ext.lower()
    d=hashlib.md5(str(datetime.datetime.now())+filename).hexdigest()
    return d+ext


def valor_equipo_componentes(equipo):
    res=list(equipocom_model.objects.filter(equipo=equipo))
    precio=0
    for x in res:
        precio+=x.componente.CO_PRECIO
    return precio