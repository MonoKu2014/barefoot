from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..model.marca import marca_model
from ..model.proveedor import proveedor_model
from ..model.tipoc import tipoc_model
from ..model.equipocom import equipocom_model
from ..model.componente import componente_model
from ..forms.componente import componente_form
from django.db import connection

def index(request):
    componentes=list(componente_model.objects.all())
    t=get_template('componentes/index.html')
    return HttpResponse(t.render({'data':componentes},request))


def edit(request,id):

    obj=get_object_or_404(componente_model,CO_ID=id)
    count=componente_count(obj)
    countr=repuestos_count(obj)
    f=componente_form(instance=obj,initial={'proveedores':obj.proveedor_id,'marcas':obj.marca_id,'tipoc':obj.tipoc_id})
    t=get_template('componentes/create.html')
    return HttpResponse(t.render({'form':f,'count':count,'countr':countr},request))

def create(request):
    count=0
    countr=0
    if request.method=='POST':
      f=componente_form(request.POST)
      if f.is_valid():
          id=request.POST['CO_ID']
          m=f.save(commit=False)
          m.marca=marca_model.objects.get(id=request.POST['marcas'])
          m.proveedor=proveedor_model.objects.get(PV_RUT=request.POST['proveedores'])
          m.tipoc=tipoc_model.objects.get(TC_ID=request.POST['tipoc'])
          if id!='':
              m.CO_ID=id
          try:
            m.save()
          except:
              print connection.queries[-1]
              print "error"
          return redirect('/componentes')
      else:
          id=request.POST['CO_ID']
          if id!='':
              comp=get_object_or_404(componente_model,CO_ID=id)
              count=componente_count(comp)
              countr=repuestos_count(comp)

    else:
      f=componente_form()
    t=get_template('componentes/create.html')
    return HttpResponse(t.render({'form':f,'count':count,'countr':countr},request))

def delete(request,id):
    obj=get_object_or_404(componente_model,CO_ID=id)
    obj.delete()
    return redirect('/componentes')


def componente_count(comp):

    return equipocom_model.objects.filter(componente=comp,EC_REPUESTO_ASIGNADO=0).count()

def repuestos_count(comp):

    return equipocom_model.objects.filter(componente=comp,EC_REPUESTO_ASIGNADO=1).count()

def can_delete(request,id):
    count=equipocom_model.objects.filter(componente=componente_model.objects.get(CO_ID=id)).count()
    return HttpResponse(count)