from django import template

register = template.Library()

@register.simple_tag
def id_in_cm_equipos(EQ_ID,equipos):
    res=equipos.all().filter(EQ_ID=EQ_ID).count()
    if res>0:
        return "<i class='icon-ok' style='color:#00a275 !important'></i>"
    return "<i class='icon-remove' style='color:red !important'></i>"
