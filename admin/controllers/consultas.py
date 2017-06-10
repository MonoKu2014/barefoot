from django.http import HttpResponse
from django.template.loader import get_template
from ..repositories.equipos import equipo_repository
from ..repositories.comunidades import comunidades_repository
from itertools import chain
from io import BytesIO
from reportlab.pdfgen import canvas
from ..utils.utils import valor_equipo_componentes
import locale
locale.setlocale(locale.LC_ALL, '')


def equipos_comunidades(request):
    rs=equipo_repository()
    rs2=comunidades_repository()
    comunidades=rs2.get_comunidades_by_pais(request.session['pais_seleccionado'])
    equipos=rs.equipos_by_pais_comunidades(comunidades)
    for x in comunidades:
        x.valor_equipos=0
        x.numero_equipos=0
        for y in x.equipos.all():
          x.numero_equipos+=1
          x.valor_equipos+=valor_equipo_componentes(y)


    t=get_template('consultas/equipos_comunidades.html')
    return HttpResponse(t.render({'comunidades':comunidades,'equipos':equipos},request))





def equipos_comunidades_pdf(request, *args, **kwargs):

    rs=equipo_repository()
    rs2=comunidades_repository()
    comunidades=rs2.get_comunidades_by_pais(request.session['pais_seleccionado'])
    equipos=rs.equipos_by_pais_comunidades(comunidades)

    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 16)
    pdf.drawString(230, 790, u"Reporte")
    pdf.setFont("Helvetica", 14)
    pdf.drawString(200, 770, u"Equipos por Comunidad")
    pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


# def tabla_comunidades_equipos(pdf,equipos,comunidades):
#     encabezado=['#']
