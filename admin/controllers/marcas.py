from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..forms.marca import marca_form
from ..model.marca import marca_model
from ..model.componente import componente_model

def index(request):
    marcas=list(marca_model.objects.all())
    t=get_template('marcas/index.html')
    return HttpResponse(t.render({'data':marcas},request))


def edit(request,id):

    obj=get_object_or_404(marca_model,id=id)
    f=marca_form(instance=obj)
    t=get_template('marcas/create.html')
    return HttpResponse(t.render({'form':f},request))

def create(request):
    if request.method=='POST':
      f=marca_form(request.POST)
      if f.is_valid():
          id=request.POST['id']
          m=f.save(commit=False)
          if id!='':
              m.id=id
          m.save()
          return redirect('/marcas')
    else:
      f=marca_form()
    t=get_template('marcas/create.html')
    return HttpResponse(t.render({'form':f},request))

def delete(request,id):
    obj=get_object_or_404(marca_model,id=id)
    obj.delete()
    return redirect('/marcas')


def can_delete(request,id):
    marca=get_object_or_404(marca_model,id=id)
    count=componente_model.objects.filter(marca=marca).count()
    return HttpResponse(count)