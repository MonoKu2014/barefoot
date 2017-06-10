from django.http import HttpResponse
from django.template.loader import get_template
from ..model.rol import rol_model
from ..forms.rol import roles_form
from django.shortcuts import redirect,get_object_or_404
from ..model.rol_modulo import rol_modulo_model
from ..model.modulo import modulo_model
from django.db import DatabaseError, transaction
import datetime

def index(request):

    data=list(rol_model.objects.all())
    t=get_template("roles/index.html")
    return HttpResponse(t.render({'data':data},request))


def create(request):

   if request.method=='POST':
      f=roles_form(request.POST)
      if f.is_valid():
          fecha=datetime.datetime
          id=request.POST['id']
          m=f.save(commit=False)
          if id != '':
              m.id=id
              m.fecha_actualizacion=fecha
          else:
              m.fecha_creacion=fecha
          m.save()
          return  redirect('/roles')
   else:
      f=roles_form()
   t=get_template("roles/create.html")
   return HttpResponse(t.render({'form':f},request))


def edit(request,id):
    obj=get_object_or_404(rol_model,id=id)
    f=roles_form(instance=obj)
    t=get_template('roles/create.html')
    return HttpResponse(t.render({'form':f},request))


def delete(request,id):
    obj=get_object_or_404(rol_model,id=id)
    obj.delete()
    return redirect('/roles')



def modulos(request,id):

    if request.method == 'POST':
        final_ids=request.POST['submodulos_ids']
        rol_id=request.POST['rol_id']
        rol=get_object_or_404(rol_model,id=rol_id)

        spl=final_ids.split('_')
        grouping={}
        if final_ids != '':
            for s in spl:
                curr=s.split('&')
                if curr[0] in grouping:
                    grouping[curr[0]].append(curr[1])
                else:
                    grouping[curr[0]]=[curr[1]]

        keys=grouping.keys()
        try:
            with transaction.atomic():
                rol_modulo_model.objects.filter(roles_id=id).delete()
                for k in keys:
                    inst=rol_modulo_model()
                    inst.modulos_id=k
                    inst.roles=rol
                    for c in grouping[k]:
                        if c == 'create':
                            inst.create = 1
                        elif c == 'update':
                            inst.update = 1
                        elif c == 'delete':
                            inst.delete = 1
                        elif c == 'pdf':
                            inst.pdf = 1
                        elif c == 'excel':
                            inst.excel = 1
                        elif c == 'assign':
                            inst.assign = 1
                    inst.save()
                return redirect('/roles')
        except DatabaseError:
           return 'errorsh'
    m=list(modulo_model.objects.all())
    r=list(rol_modulo_model.objects.filter(roles_id=id))
    t=get_template('roles/modulos.html')
    return HttpResponse(t.render({'modulos':m,'roles':r,'rol_id':id},request))
