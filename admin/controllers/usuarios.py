from django.http import HttpResponse
from django.template.loader import get_template
from ..forms.usuario import usuario_form
from django.shortcuts import redirect,get_object_or_404
from ..model.usuario import usuario_model
from ..model.pais import pais_model
from ..model.rol import rol_model
from ..model.usuario import usuarios_paises_model
from ..repositories.pais import pais_repository
import datetime

def index(request):
    ing=get_ing_solar()
    usuarios=list(usuario_model.objects.all())
    t=get_template('usuarios/index.html')
    return HttpResponse(t.render({'data':usuarios,'ing':ing},request))

def edit(request,id):

    obj=get_object_or_404(usuario_model,id=id)
    ing=get_ing_solar()
    f=usuario_form(instance=obj,initial={'roles':obj.rol_id,'paises':obj.pais_id})
    t=get_template('usuarios/create.html')
    return HttpResponse(t.render({'form':f,'ing':ing},request))

def create(request):
    ing=get_ing_solar()

    if request.method=='POST':
      rol_id=request.POST['roles']
      f=usuario_form(request.POST)
      if rol_id != '8':
          f.ing_precio_dia=0
          if 'ing_precio_dia' in f.errors:
            del f.errors['ing_precio_dia']
      if f.is_valid():
          fecha=datetime.datetime
          id=request.POST['id']

          pais=pais_model.objects.get(PA_ID=request.POST['paises'])
          m=f.save(commit=False)
          m.pais=pais

          m.rol_id=rol_id
          if id != '':
            m.id=id
            m.fecha_actualizacion=fecha
          else:
            m.fecha_creacion=fecha
          m.save()
          return redirect('/usuarios')
    else:
      f=usuario_form

    t=get_template('usuarios/create.html')
    return HttpResponse(t.render({'form':f,'ing':ing},request))

def delete(request,id):
    obj=get_object_or_404(usuario_model,id=id)
    obj.delete()
    return redirect('/usuarios')


def get_ing_solar():
    return get_object_or_404(rol_model,ing_solar=1)


def paises(request,id):

    all=pais_model.objects.all()
    obj=get_object_or_404(usuario_model,id=id)
    if request.method == 'POST':
        pais_sel=pais_model.objects.get(PA_ID=request.POST['pais'])
        model=usuarios_paises_model()
        model.paises=pais_sel
        model.usuarios=obj
        try:
          model.save()
        except :
          from django.db import connection
          print connection.queries[-1]
    paises=list(obj.paises.all())
    final_paises=[x for x in all if x != obj.pais and x not in paises]

    t=get_template('usuarios/paises.html')
    return HttpResponse(t.render({'paises':final_paises,'usuario':obj,'paises_asignados':paises},request))


def paises_delete(request,id_usuario,id_pais):
    pais=get_object_or_404(pais_model,PA_ID=id_pais)
    usuario=get_object_or_404(usuario_model,id=id_usuario)
    usuario_pais=get_object_or_404(usuarios_paises_model,usuarios=usuario,paises=pais)
    usuario_pais.delete()
    return redirect('/usuarios/paises/'+str(id_usuario))
