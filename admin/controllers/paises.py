from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..forms.pais import pais_form
from ..model.pais import pais_model
from ..model.comunidad import comunidad_model

def index(request):
    paises=list(pais_model.objects.all())
    t=get_template('paises/index.html')
    return HttpResponse(t.render({'data':paises},request))


def edit(request,id):

    obj=get_object_or_404(pais_model,PA_ID=id)
    f=pais_form(instance=obj)
    t=get_template('paises/create.html')
    return HttpResponse(t.render({'form':f},request))

def create(request):
    if request.method=='POST':
      f=pais_form(request.POST)
      if f.is_valid():
          id=request.POST['PA_ID']
          m=f.save(commit=False)
          if id!='':
              m.PA_ID=id
          m.save()
          return redirect('/paises')
    else:
      f=pais_form()
    t=get_template('paises/create.html')
    return HttpResponse(t.render({'form':f},request))

def delete(request,id):
    obj=get_object_or_404(pais_model,PA_ID=id)
    obj.delete()
    return redirect('/paises')

def can_delete(request,id):
    pais=get_object_or_404(pais_model,PA_ID=id)
    count=comunidad_model.objects.filter(pais=pais).count()
    return HttpResponse(count)