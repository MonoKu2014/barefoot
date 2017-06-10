from django import template

register = template.Library()



@register.simple_tag
def submodule_match(roles_modulos,submodulo,cond):
    if cond=='create':
      f=[(x.id)for x in roles_modulos if x.modulos == submodulo and x.create == 1]
    elif cond=='update':
      f=[(x.id)for x in roles_modulos if x.modulos == submodulo and x.update == 1]
    elif cond=='delete':
      f=[(x.id)for x in roles_modulos if x.modulos == submodulo and x.delete == 1]
    elif cond=='pdf':
      f=[(x.id)for x in roles_modulos if x.modulos == submodulo and x.pdf == 1]
    elif cond=='excel':
      f=[(x.id)for x in roles_modulos if x.modulos == submodulo and x.excel == 1]
    elif cond=='assign':
      f=[(x.id)for x in roles_modulos if x.modulos == submodulo and x.assign == 1]


    if len(f) > 0:
        return "<input type='hidden' class='ids' value='"+str(submodulo.id)+"&"+cond+"'/>" \
               "<input type='checkbox' class='subm'  checked='checked' ><span class='toggle'>"
    return "<input type='hidden' class='ids' value='"+str(submodulo.id)+"&"+cond+"'/>" \
           "<input type='checkbox' class='subm'><span class='toggle'>"

@register.simple_tag(takes_context=True)
def show_title(context,nombre):
    request=context['request']
    submodulos=request.session['submodulos']
    res=[(x.id,x.nombre)for x in submodulos if x.modulo.nombre == nombre]
    if len(res) > 0:
        return True
    return False

@register.simple_tag(takes_context=True)
def show_action(context,submodulo,cond):
    request=context['request']
    submodulos=request.session['roles_usuario']
    if cond == 'create':
        f = [x.id for x in submodulos if x.modulos.nombre == submodulo and x.create == 1]
    elif cond == 'update':
        f = [x.id for x in submodulos if x.modulos.nombre == submodulo and x.update == 1]
    elif cond == 'delete':
        f = [x.id for x in submodulos if x.modulos.nombre == submodulo and x.delete == 1]
    elif cond == 'pdf':
        f = [x.id for x in submodulos if x.modulos.nombre == submodulo and x.pdf == 1]
    elif cond == 'excel':
        f = [x.id for x in submodulos if x.modulos.nombre == submodulo and x.excel == 1]
    elif cond == 'assign':
        f = [x.id for x in submodulos if x.modulos.nombre == submodulo and x.assign == 1]
    if len(f) > 0:
        return True
    return False

@register.simple_tag(takes_context=True)
def show_module(context,nombre_bd):
    request=context['request']
    submodulos=request.session['submodulos']
    res=[(x.id,x.nombre)for x in submodulos if x.nombre == nombre_bd]
    if len(res) > 0:
        return True
    return False