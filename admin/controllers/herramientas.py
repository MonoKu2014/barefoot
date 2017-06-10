from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..forms.herramienta import herramienta_form
from ..model.herramienta import herramienta_model
from ..model.componente import componente_model

def index(request):
    herramientas=list(herramienta_model.objects.all())
    t=get_template('herramientas/index.html')
    return HttpResponse(t.render({'data':herramientas},request))


def edit(request,id):

    obj=get_object_or_404(herramienta_model,HR_ID=id)
    f=herramienta_form(instance=obj,initial={'componentes':obj.componente.CO_ID})
    t=get_template('herramientas/create.html')
    return HttpResponse(t.render({'form':f},request))

def create(request):
    if request.method=='POST':
      f=herramienta_form(request.POST)
      if f.is_valid():
          id=request.POST['HR_ID']
          m=f.save(commit=False)
          m.componente=componente_model.objects.get(CO_ID=request.POST['componentes'])
          if id!='':
              m.HR_ID=id
          m.save()
          return redirect('/herramientas')
    else:
      f=herramienta_form()
    t=get_template('herramientas/create.html')
    return HttpResponse(t.render({'form':f},request))

def delete(request,id):
    obj=get_object_or_404(herramienta_model,HR_ID=id)
    obj.delete()
    return redirect('/herramientas')