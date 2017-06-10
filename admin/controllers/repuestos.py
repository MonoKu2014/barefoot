# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.shortcuts import redirect,get_object_or_404
# from ..model.marca import marca_model
# from ..model.proveedor import proveedor_model
# from ..model.tipoc import tipoc_model
# from ..forms.repuesto import repuesto_form
# from ..model.repuestos import repuesto_model
# from django.db import connection
#
# def index(request):
#     repuestos=list(repuesto_model.objects.all())
#     t=get_template('repuestos/index.html')
#     return HttpResponse(t.render({'data':repuestos},request))
#
#
# def edit(request,id):
#
#     obj=get_object_or_404(repuesto_model,RE_ID=id)
#     f=repuesto_form(instance=obj,initial={'proveedores':obj.proveedor.PV_ID,'marcas':obj.marca.id,'tipoc':obj.tipoc.TC_ID})
#     t=get_template('repuestos/create.html')
#     return HttpResponse(t.render({'form':f},request))
#
# def create(request):
#     if request.method=='POST':
#       f=repuesto_form(request.POST)
#       if f.is_valid():
#           id=request.POST['RE_ID']
#           m=f.save(commit=False)
#           m.marca=marca_model.objects.get(id=request.POST['marcas'])
#           m.proveedor=proveedor_model.objects.get(PV_ID=request.POST['proveedores'])
#           m.tipoc=tipoc_model.objects.get(TC_ID=request.POST['tipoc'])
#           if id!='':
#               m.RE_ID=id
#           try:
#             m.save()
#           except:
#               print connection.queries[-1]
#               print "error"
#           return redirect('/repuestos')
#     else:
#       f=repuesto_form()
#     t=get_template('repuestos/create.html')
#     return HttpResponse(t.render({'form':f},request))
#
# def delete(request,id):
#     obj=get_object_or_404(repuesto_model,RE_ID=id)
#     obj.delete()
#     return redirect('/repuestos')