from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import  get_template
from ..forms.login import login_form
from ..model.usuario import usuario_model
from ..model.pais import pais_model
from ..model.rol_modulo import rol_modulo_model
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
import hashlib

def login(request):
    if request.method=='POST':
      f=login_form(request.POST)
      if f.is_valid():
          try:
              user=usuario_model.objects.get(usuario=request.POST['usuario'],password=request.POST['password'])
              user.password=''
              if user.rol.ing_solar==1:
                  paises=pais_model.objects.filter(PA_ID=user.pais.PA_ID)
                  request.session['pais_seleccionado']=paises[0]
              else:
                  paises=list(user.paises.all())
                  paises.append(user.pais)
                  request.session['pais_seleccionado']=user.pais

              roles_usuario=list(rol_modulo_model.objects.filter(roles_id=user.rol.id))
              submodulos=list(user.rol.submodulos.all())
              request.session['paises']=paises
              request.session['user']=user
              request.session['submodulos']=submodulos
              request.session['roles_usuario']=roles_usuario


              return redirect('/dashboard')
          except ObjectDoesNotExist:
              f.errors.notExists='El usuario no Existe en el sistema'
    else:
      f=login_form
    t=get_template('frontend/login.html')
    return HttpResponse(t.render({'form':f},request))


def dashboard(request):
    t=get_template("frontend/dashboard.html")
    return HttpResponse(t.render({},request))


def reset_password(request):
    try:
      email=request.POST['email']
      email_db=usuario_model.objects.get(email=email)

      pass_cifrado = hashlib.md5(email_db.usuario).hexdigest()[0:5]

      email_db.codigo_password=pass_cifrado
      email_db.save()

      mail = EmailMessage('Recuperacion de Password',
                        'El codigo de recuperacion es '+email_db.codigo_password+', Ingreselo porfavor en la pantalla principal',
                        to=[email_db.email],
                        from_email='Barefoot@admin.cl')
      mail.send()
      return HttpResponse('SUCCESS')
    except ObjectDoesNotExist:
      return HttpResponse('ERROR01')

def check_code(request):

    try:
      email=request.POST['email']
      code=request.POST['codigo']

      usuario=usuario_model.objects.get(email=email,codigo_password=code)
      usuario.password=code
      usuario.save()
      return HttpResponse('SUCCESS')
    except ObjectDoesNotExist:
      return HttpResponse('ERROR01')


def exit(request):
    del request.session['user']
    return redirect('/')

def cambio_pais(request):
    id_pais=request.POST['id_pais']

    ps=[x for x in request.session['paises'] if x.PA_ID == int(id_pais)][0]

    request.session['pais_seleccionado']=ps
    return redirect('/dashboard')
