from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..model.comunidad import comunidad_model
from ..forms.comunidad import comunidad_form
from ..model.equipo import equipo_model
from ..model.comunidad import equipo_comunidades_model
from django.db import connection
from ..model.pais import pais_model
from ..utils.fileupload import handle_uploaded_file
from ..utils.utils import ext_md5_file
from ..model.taller_solar import taller_solar_model
from ..forms.taller_solar import taller_solar_form

def index(request):
    comunidades=list(comunidad_model.objects.filter(pais=request.session['pais_seleccionado']))
    t=get_template('comunidades/index.html')
    return HttpResponse(t.render({'data':comunidades},request))


def edit(request,id):

    obj=get_object_or_404(comunidad_model,CM_ID=id)
    f=comunidad_form(instance=obj,initial={'paises':obj.pais.PA_ID,'CM_FIRMADO':bool(obj.CM_FIRMADO),'CM_RESERVADO':bool(obj.CM_RESERVADO)})
    t=get_template('comunidades/create.html')
    return HttpResponse(t.render({'form':f},request))



def create(request):

    if request.method=='POST':
        f=comunidad_form(request.POST,request.FILES)
        if f.is_valid():
            m=f.save(commit=False)

            if  request.FILES.get('CM_DOC_DONACION_COMITE') is not None:
                _CM_DOC_DONACION_COMITE=ext_md5_file(request.FILES['CM_DOC_DONACION_COMITE'].name)
                handle_uploaded_file(request.FILES['CM_DOC_DONACION_COMITE'],'admin/static/upload/acta donacion con comite/'+_CM_DOC_DONACION_COMITE)
                m.CM_DOC_DONACION_COMITE=_CM_DOC_DONACION_COMITE


            if  request.FILES.get('CM_DOC_CMI')is not None:
                _CM_DOC_CMI=ext_md5_file(request.FILES['CM_DOC_CMI'].name)
                handle_uploaded_file(request.FILES['CM_DOC_CMI'],'admin/static/upload/contrato mantencion ingeniera/'+_CM_DOC_CMI)
                m.CM_DOC_CMI=_CM_DOC_CMI

            if  request.FILES.get('CM_DOC_CUENTA_BANCARIA')is not None:
                _CM_DOC_CUENTA_BANCARIA=ext_md5_file(request.FILES['CM_DOC_CUENTA_BANCARIA'].name)
                handle_uploaded_file(request.FILES['CM_DOC_CUENTA_BANCARIA'],'admin/static/upload/contrato de personalidad juridica/'+_CM_DOC_CUENTA_BANCARIA)
                m.CM_DOC_CUENTA_BANCARIA=_CM_DOC_CUENTA_BANCARIA

            id=request.POST['CM_ID']
            m.pais=get_object_or_404(pais_model,PA_ID=request.POST['paises'])
            m.CM_PAIS=request.POST['paises']

            if id!='':
                _cm=get_object_or_404(comunidad_model,CM_ID=id)

                if m.CM_DOC_DONACION_COMITE is None or  not m.CM_DOC_DONACION_COMITE:
                    if _cm.CM_DOC_DONACION_COMITE is not None:
                        m.CM_DOC_DONACION_COMITE= _cm.CM_DOC_DONACION_COMITE
                    else:
                        m.CM_DOC_DONACION_COMITE=None

                if m.CM_DOC_CMI is None or not m.CM_DOC_CMI:
                    if _cm.CM_DOC_CMI is not None:
                        m.CM_DOC_CMI=_cm.CM_DOC_CMI
                    else:
                        m.CM_DOC_CMI=None

                if m.CM_DOC_CUENTA_BANCARIA is None or not m.CM_DOC_CUENTA_BANCARIA:
                    if _cm.CM_DOC_CUENTA_BANCARIA is not None:
                        m.CM_DOC_CUENTA_BANCARIA= _cm.CM_DOC_CUENTA_BANCARIA
                    else:
                        m.CM_DOC_CUENTA_BANCARIA=None
                m.CM_ID=id

            else:
                if m.CM_DOC_DONACION_COMITE is None or not m.CM_DOC_DONACION_COMITE:
                        m.CM_DOC_DONACION_COMITE=None
                if m.CM_DOC_CMI is None or not m.CM_DOC_CMI:
                       m.CM_DOC_CMI=None
                if m.CM_DOC_CUENTA_BANCARIA is None or not m.CM_DOC_CUENTA_BANCARIA:
                       m.CM_DOC_CUENTA_BANCARIA=None

            m.save()
            return redirect('/comunidades')
        else:
            id=request.POST['CM_ID']
            if id!='':
                f.instance.CM_DOC_DONACION_COMITE=None
                _cm=get_object_or_404(comunidad_model,CM_ID=id)
                if f.instance.CM_DOC_DONACION_COMITE is None or not f.instance.CM_DOC_DONACION_COMITE:
                    if _cm.CM_DOC_DONACION_COMITE is not None:
                        f.instance.CM_DOC_DONACION_COMITE=_cm.CM_DOC_DONACION_COMITE
                    else:
                       f.instance.CM_DOC_DONACION_COMITE=None

                if f.instance.CM_DOC_CMI is None or not f.instance.CM_DOC_CMI:
                    if _cm.CM_DOC_CMI is not None:
                        f.instance.CM_DOC_CMI=_cm.CM_DOC_CMI
                    else:
                       f.instance.CM_DOC_CMI=None


                if f.instance.CM_DOC_CUENTA_BANCARIA is None or not f.instance.CM_DOC_CUENTA_BANCARIA:
                    if _cm.CM_DOC_CUENTA_BANCARIA is not None:
                        f.instance.CM_DOC_CUENTA_BANCARIA=_cm.CM_DOC_CUENTA_BANCARIA
                    else:
                       f.instance.CM_DOC_CUENTA_BANCARIA=None

            else:

                f.instance.CM_DOC_DONACION_COMITE=None
                f.instance.CM_DOC_CMI=None
                f.instance.CM_DOC_CUENTA_BANCARIA=None

    else:
        f=comunidad_form()
    t=get_template('comunidades/create.html')
    return HttpResponse(t.render({'form':f},request))


def delete(request,id):
    obj=get_object_or_404(comunidad_model,CM_ID=id)
    obj.delete()
    return redirect('/comunidades')

def equipos(request,id):
    obj=get_object_or_404(comunidad_model,CM_ID=id)
    if request.method=='POST':
        id_equipo=request.POST['equipo']
        m=equipo_comunidades_model()
        eq=get_object_or_404(equipo_model,EQ_ID=id_equipo)
        m.equipos=eq
        m.comunidades=obj
        try:
          m.save()
        except :
          from django.db import connection
          print connection.queries[-1]
    equipos_comunidad=list(obj.equipos.all())
    equipos=list(equipo_model.objects.all())
    final_equipos=[x for  x in equipos if x not in equipos_comunidad]

    t=get_template('comunidades/equipos.html')
    return HttpResponse(t.render({'equipos':final_equipos,'equipos_asignados':equipos_comunidad,'CM_ID':id},request))

def delete_equipo(request,id_comunidad,id_equipo):
    obj=get_object_or_404(comunidad_model,CM_ID=id_comunidad)
    eq=get_object_or_404(equipo_model,EQ_ID=id_equipo)
    model=get_object_or_404(equipo_comunidades_model,equipos=eq,comunidades=obj)
    model.delete()

    return redirect('/comunidades/equipos/'+str(id_comunidad))


def can_delete(request,id):
    com=comunidad_model.objects.get(CM_ID=id)
    count=equipo_comunidades_model.objects.filter(comunidades=com).count()
    return HttpResponse(count)


def taller_solar(request,id):
    cm=comunidad_model()
    cm.CM_ID=id

    if request.method=='POST':
        form=taller_solar_form(request.POST)
        if form.is_valid():
            m=form.save(commit=False)
            m.comunidad=cm
            taller_id=request.POST['TS_ID']

            if taller_id!='':
                 m.TS_ID=taller_id
            m.save()
            return redirect('/comunidades')

    else:
      try:
        taller_solar=taller_solar_model.objects.get(comunidad=cm)
        form=taller_solar_form(instance=taller_solar,initial={'TS_HABILITADO':bool(taller_solar.TS_HABILITADO)})
      except:
        form=taller_solar_form()

    t=get_template('comunidades/taller_solar.html')
    return HttpResponse(t.render({'form':form,'CM_ID':id},request))
