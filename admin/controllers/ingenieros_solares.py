from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..model.usuario import usuario_model
from ..model.pais import pais_model
from ..model.ingeniero_solar import ingeniero_solar_model
from ..forms.ingeniero_solar import ingeniero_solar_form

def index(request):
    ingenieros=list(ingeniero_solar_model.objects.all())
    t=get_template('ingenieros_solares/index.html')
    return HttpResponse(t.render({'data':ingenieros},request))


def edit(request,id):

    obj=get_object_or_404(ingeniero_solar_model,ING_ID=id)
    f=ingeniero_solar_form(instance=obj,initial={'usuarios': obj.usuario.id,'paises':obj.pais.PA_ID})
    t=get_template('ingenieros_solares/create.html')
    return HttpResponse(t.render({'form':f},request))

def create(request):
    if request.method=='POST':
      f=ingeniero_solar_form(request.POST)
      if f.is_valid():
          id=request.POST['ING_ID']
          m=f.save(commit=False)
          m.pais=pais_model.objects.get(PA_ID=request.POST['paises'])
          m.usuario=usuario_model.objects.get(id=request.POST['usuarios'])
          if id!='':
              m.ING_ID=id
          m.save()
          return redirect('/ingenieros_solares')
    else:
      f=ingeniero_solar_form()
    t=get_template('ingenieros_solares/create.html')
    return HttpResponse(t.render({'form':f},request))

def delete(request,id):
    obj=get_object_or_404(pais_model,PA_ID=id)
    obj.delete()
    return redirect('/ingenieros_solares')
