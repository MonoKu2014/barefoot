from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..forms.proveedor import proveedor_form
from ..model.proveedor import proveedor_model

def index(request):
    proveedores=list(proveedor_model.objects.all())
    t=get_template('proveedores/index.html')
    return HttpResponse(t.render({'data':proveedores},request))


def edit(request,id):

    obj=get_object_or_404(proveedor_model,PV_ID=id)
    f=proveedor_form(instance=obj)
    t=get_template('proveedores/create.html')
    return HttpResponse(t.render({'form':f},request))

def create(request):
    if request.method=='POST':
      f=proveedor_form(request.POST)
      if f.is_valid():
          id=request.POST['PV_ID']
          m=f.save(commit=False)
          if id!='':
              m.PV_ID=id
          m.save()
          return redirect('/proveedores')
    else:
      f=proveedor_form()
    t=get_template('proveedores/create.html')
    return HttpResponse(t.render({'form':f},request))

def delete(request,id):
    obj=get_object_or_404(proveedor_model,PV_ID=id)
    obj.delete()
    return redirect('/proveedores')