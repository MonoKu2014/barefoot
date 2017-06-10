from django import template
import os

register = template.Library()

@register.simple_tag
def icon_doc(nombre):

    ext=os.path.splitext(nombre)[1].lower()
    if ext.lower()=='.pdf':
        return "<i style='color:red' class='fa fa-file-pdf-o  fa-2x' aria-hidden='true'></i>"
    elif ext.lower() == '.doc' or ext.lower() == '.docx':
        return "<i style='color:blue' class='fa fa-file-word-o  fa-2x' aria-hidden='true'></i>"

