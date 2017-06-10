from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect,get_object_or_404
from ..model.equipo import equipo_model
from ..forms.equipo import equipo_form
from ..model.tipoe import tipoe_model
from ..model.equipocom import equipocom_model
from ..repositories.equipos import equipo_repository
from ..repositories.comunidades import comunidades_repository
from ..repositories.componente import componente_repository
from ..model.componente import componente_model
from ..utils.utils import ext_md5_file
from ..utils.fileupload import handle_uploaded_file
from ..utils.utils import valor_equipo_componentes


def index(request):

    rs=equipo_repository()
    rs2=comunidades_repository()

    comunidades=rs2.get_comunidades_by_pais(request.session['pais_seleccionado'])
    equipos=rs.equipos_by_pais_comunidades(comunidades)
    for u in equipos:
        u.num_componentes=0
        u.num_componentes=equipocom_model.objects.filter(equipo=u).count()

    t=get_template('equipos/index.html')
    return HttpResponse(t.render({'data':equipos},request))


def edit(request,id):

    obj=get_object_or_404(equipo_model,EQ_ID=id)
    f=equipo_form(instance=obj,initial={'tipoe':obj.tipoe.TE_ID,'EQ_ESTADO':bool(obj.EQ_ESTADO)})
    t=get_template('equipos/create.html')
    return HttpResponse(t.render({'form':f},request))



def create(request):
    if request.method=='POST':
      f=equipo_form(request.POST,request.FILES)
      if f.is_valid():
          m=f.save(commit=False)
          if  request.FILES.get('EQ_DOC_CONTRATO') is not None:
              _EQ_DOC_CONTRATO=ext_md5_file(request.FILES['EQ_DOC_CONTRATO'].name)
              handle_uploaded_file(request.FILES['EQ_DOC_CONTRATO'],'admin/static/upload/contrato equipo/'+_EQ_DOC_CONTRATO)
              m.EQ_DOC_CONTRATO=_EQ_DOC_CONTRATO

          id=request.POST['EQ_ID']
          m.tipoe=get_object_or_404(tipoe_model,TE_ID=request.POST['tipoe'])
          if id!='':
              _eq=get_object_or_404(equipo_model,EQ_ID=id)

              if m.EQ_DOC_CONTRATO is None or  not m.EQ_DOC_CONTRATO:
                  if _eq.EQ_DOC_CONTRATO is not None:
                        m.EQ_DOC_CONTRATO= _eq.EQ_DOC_CONTRATO
                  else:
                        m.EQ_DOC_CONTRATO=None


              m.EQ_ID=id

          else:
              if m.EQ_DOC_CONTRATO is None or not m.EQ_DOC_CONTRATO:
                  m.EQ_DOC_CONTRATO=None

          m.EQ_PRECIO=0
          m.save()
          return redirect('/equipos')

      else:
            id=request.POST['EQ_ID']
            if id!='':
                _cm=get_object_or_404(equipo_model,EQ_ID=id)
                if f.instance.EQ_DOC_CONTRATO is None or not f.instance.EQ_DOC_CONTRATO:
                    if _cm.EQ_DOC_CONTRATO is not None:
                        f.instance.EQ_DOC_CONTRATO=_cm.EQ_DOC_CONTRATO
            else:
                f.instance.EQ_DOC_CONTRATO=None
    else:
      f=equipo_form()
    t=get_template('equipos/create.html')
    return HttpResponse(t.render({'form':f},request))

def valor_componente(equipo):
     return valor_equipo_componentes(equipo)



def delete(request,id):
    obj=get_object_or_404(equipo_model,EQ_ID=id)
    obj.delete()
    return redirect('/equipos')


def componentes(request,id):

    rs=componente_repository()
    obj=get_object_or_404(equipo_model,EQ_ID=id)
    if request.method=='POST':

        m=equipocom_model()
        comp_id=request.POST['componente']
        comp=get_object_or_404(componente_model,CO_ID=comp_id)
        m.equipo=obj
        m.componente=comp
        try:
          m.save()
        except :
          from django.db import connection
          print connection.queries[-1]

    com=list(equipocom_model.objects.filter(equipo=obj))
    comps=componente_model.objects.all()

    only_comp=[]
    for x in com:
        only_comp.append({"componente":x.componente,'repuesto':x.EC_REPUESTO_ASIGNADO})
    final_comps=[x for  x in comps if x not in only_comp]
    t=get_template('equipos/componentes.html')
    return HttpResponse(t.render({'comps_list':final_comps,'comps_assign':only_comp,'EQ_ID':id},request))

def delete_componente(request,equipo_id,componente_id):
    obj=get_object_or_404(equipo_model,EQ_ID=equipo_id)
    co=get_object_or_404(componente_model,CO_ID=componente_id)
    model=get_object_or_404(equipocom_model,equipo=obj,componente=co)
    model.delete()
    return redirect('/equipos/componentes/'+str(equipo_id))


def repuestos(request,id):

    rs=componente_repository()
    obj=get_object_or_404(equipo_model,EQ_ID=id)

    if request.method=='POST':

        comp_id=request.POST['componente']
        comp=get_object_or_404(componente_model,CO_ID=comp_id)

        m=equipocom_model.objects.get(equipo=obj,componente=comp)
        m.EC_REPUESTO_ASIGNADO=1

        try:
          m.save()
        except :
          from django.db import connection
          print connection.queries[-1]


    com_all=list(equipocom_model.objects.filter(equipo=obj))
    _com_list=[x for x in com_all if x.EC_REPUESTO_ASIGNADO == 0]
    _com_sel=[x for x in com_all if x.EC_REPUESTO_ASIGNADO == 1]

    com_list=[x.componente for x in _com_list]
    com_sel=[x.componente for x in _com_sel]
    t=get_template('equipos/repuestos.html')
    return HttpResponse(t.render({'comps_list':com_list,
                                  'comps_assign':com_sel,
                                  'EQ_ID':id},request))


def delete_repuesto(request,equipo_id,componente_id):
    obj=get_object_or_404(equipo_model,EQ_ID=equipo_id)
    co=get_object_or_404(componente_model,CO_ID=componente_id)
    model=get_object_or_404(equipocom_model,equipo=obj,componente=co)
    model.EC_REPUESTO_ASIGNADO=0
    model.save()
    return redirect('/equipos/repuestos/'+str(equipo_id))


def can_delete(request,id):
    count=equipocom_model.objects.filter(equipo=equipo_model.objects.get(EQ_ID=id)).count()
    return HttpResponse(count)


