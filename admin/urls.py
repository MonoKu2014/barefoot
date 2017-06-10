from django.conf.urls import url
from .controllers import frontend
from .controllers import usuarios
from .controllers import roles
from .controllers import componentes
from .controllers import comunidades
from .controllers import equipos
from .controllers import paises
from .controllers import ingenieros_solares,\
                         marcas,proveedores,\
                         herramientas,\
                         consultas,\
                         repuestos


urlpatterns = [
     url(r'^$', frontend.login),
     url(r'^dashboard$', frontend.dashboard),
     url(r'^exit$', frontend.exit),
     url(r'^reset_password$', frontend.reset_password),
     url(r'^check_code$', frontend.check_code),
     url(r'^cambio_pais$', frontend.cambio_pais),

     url(r'^consultas/equipos_comunidades$',consultas.equipos_comunidades),
     url(r'^consultas/equipos_comunidades/PDF$',consultas.equipos_comunidades_pdf),

     url(r'^usuarios$',usuarios.index),
     url(r'^usuarios/create$',usuarios.create),
     url(r'^usuarios/edit/([0-9]*)$',usuarios.edit),
     url(r'^usuarios/delete/([0-9]*)$',usuarios.delete),
     url(r'^usuarios/paises/([0-9]*)$',usuarios.paises),
     url(r'^usuarios/paises/delete/([0-9]*)/([0-9]*)$',usuarios.paises_delete),

     url(r'^roles$',roles.index),
     url(r'^roles/create$',roles.create),
     url(r'^roles/edit/([0-9]*)$',roles.edit),
     url(r'^roles/delete/([0-9]*)$',roles.delete),
     url(r'^roles/modulos/([0-9]*)$',roles.modulos),

     url(r'^componentes$',componentes.index),
     url(r'^componentes/create$',componentes.create),
     url(r'^componentes/edit/([0-9]*)$',componentes.edit),
     url(r'^componentes/delete/([0-9]*)$',componentes.delete),
     url(r'^componentes/can_delete/([0-9]*)$',componentes.can_delete),

     # url(r'^repuestos$',repuestos.index),
     # url(r'^repuestos/create$',repuestos.create),
     # url(r'^repuestos/edit/([0-9]*)$',repuestos.edit),
     # url(r'^repuestos/delete/([0-9]*)$',repuestos.delete),

     url(r'^comunidades$',comunidades.index),
     url(r'^comunidades/create$',comunidades.create),
     url(r'^comunidades/edit/([0-9]*)$',comunidades.edit),
     url(r'^comunidades/delete/([0-9]*)$',comunidades.delete),
     url(r'^comunidades/equipos/([0-9]*)$',comunidades.equipos),
     url(r'^comunidades/equipos/delete/([0-9]*)/([0-9]*)$',comunidades.delete_equipo),
     url(r'^comunidades/can_delete/([0-9]*)$',comunidades.can_delete),
     url(r'^comunidades/taller_solar/([0-9]*)$',comunidades.taller_solar),


     url(r'^equipos$',equipos.index),
     url(r'^equipos/create$',equipos.create),
     url(r'^equipos/edit/([0-9]*)$',equipos.edit),
     url(r'^equipos/delete/([0-9]*)$',equipos.delete),
     url(r'^equipos/componentes/([0-9]*)$',equipos.componentes),
     url(r'^equipos/componentes/delete/([0-9]*)/([0-9]*)$',equipos.delete_componente),
     url(r'^equipos/repuestos/([0-9]*)$',equipos.repuestos),
     url(r'^equipos/repuestos/delete/([0-9]*)/([0-9]*)$',equipos.delete_repuesto),
     url(r'^equipos/can_delete/([0-9]*)$',equipos.can_delete),

     url(r'^paises$',paises.index),
     url(r'^paises/create$',paises.create),
     url(r'^paises/edit/([0-9]*)$',paises.edit),
     url(r'^paises/delete/([0-9]*)$',paises.delete),
     url(r'^paises/can_delete/([0-9]*)$',paises.can_delete),


     url(r'^ingenieros_solares$',ingenieros_solares.index),
     url(r'^ingenieros_solares/create$',ingenieros_solares.create),
     url(r'^ingenieros_solares/edit/([0-9]*)$',ingenieros_solares.edit),
     url(r'^ingenieros_solares/delete/([0-9]*)$',ingenieros_solares.delete),


     url(r'^marcas$',marcas.index),
     url(r'^marcas/create$',marcas.create),
     url(r'^marcas/edit/([0-9]*)$',marcas.edit),
     url(r'^marcas/delete/([0-9]*)$',marcas.delete),
     url(r'^marcas/can_delete/([0-9]*)$',marcas.can_delete),

     url(r'^proveedores$',proveedores.index),
     url(r'^proveedores/create$',proveedores.create),
     url(r'^proveedores/edit/([0-9]*)$',proveedores.edit),
     url(r'^proveedores/delete/([0-9]*)$',proveedores.delete),

     url(r'^herramientas$',herramientas.index),
     url(r'^herramientas/create$',herramientas.create),
     url(r'^herramientas/edit/([0-9]*)$',herramientas.edit),
     url(r'^herramientas/delete/([0-9]*)$',herramientas.delete),
]