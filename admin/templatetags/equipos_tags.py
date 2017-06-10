from django import template
from ..utils.utils import valor_equipo_componentes
import locale
locale.setlocale(locale.LC_ALL,'')

register = template.Library()

@register.simple_tag
def sum_components(eq):
    if(eq.EQ_ID is None):
        return str(0)
    else:
        return str(valor_equipo_componentes(eq))

@register.simple_tag
def num_comp_equipos(model):
    return model.equipos.count()


@register.simple_tag
def valor_equipos(model):
    res=0
    for x in model.equipos.all():
      res+=valor_equipo_componentes(x)
    return locale.format('%d',int(res),1).replace(',','.')

@register.simple_tag
def num_equipos_pais(com):
    num=0

    for x in com:
        num+=x.numero_equipos
    return locale.format('%d',int(num),1).replace(',','.')


@register.simple_tag
def valor_equipos_pais(com):
    valor=0
    loc=locale.getlocale()
    for x in com:
        valor+=x.valor_equipos
    return locale.format('%d',int(valor),1).replace(',','.')


@register.simple_tag
def format(number):
    return locale.format('%d',int(number),1).replace(',','.')