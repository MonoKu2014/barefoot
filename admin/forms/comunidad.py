from django.forms import ModelForm
from django import forms
from ..model.comunidad import comunidad_model
from ..utils import error_messages
from ..model.pais import pais_model
from ..fields.fields import ExtFileField

class comunidad_form(ModelForm):



      def __init__(self, *args, **kwargs):
        super(comunidad_form, self).__init__(*args, **kwargs)
        self.fields['paises'].choices=[(r.PA_ID,r.PA_NOMBRE)for r in pais_model.objects.all()]


      CM_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      CM_NOMBRE=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})
      CM_NUMEQUIPOS=forms.DecimalField(
          max_digits=3,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad Equipos','id':'equipos'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(3)})

      CM_CASAS=forms.DecimalField(
          max_digits=3,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad Casas','id':'casas'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(4)})

      CM_TIENDAS=forms.DecimalField(
          max_digits=3,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad Tiendas','id':'tiendas'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(4)})

      CM_EDIFICIOS=forms.DecimalField(
          max_digits=3,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad Edificios','id':'edificios'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(4)})

      CM_FIRMADO=forms.BooleanField(
          required=False,
          widget=forms.CheckboxInput(attrs={'id':'firmado'}))

      CM_RESERVADO=forms.BooleanField(
          required=False,
          widget=forms.CheckboxInput(attrs={'id':'firmado'}))

      paises=forms.ChoiceField(
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)

      CM_DOC_DONACION_COMITE=ExtFileField(
                                 required=False,
                                 ext_whitelist=['.doc','.docx','.pdf'])

      CM_DOC_CMI=ExtFileField(
                                 required=False,
                                 ext_whitelist=['.doc','.docx','.pdf'])

      CM_DOC_CUENTA_BANCARIA=ExtFileField(
                                 required=False,
                                 ext_whitelist=['.doc','.docx','.pdf'])


      class Meta:
          model=comunidad_model
          fields=('CM_ID','CM_NOMBRE','CM_NUMEQUIPOS','CM_CASAS','CM_TIENDAS','CM_EDIFICIOS','CM_FIRMADO','CM_RESERVADO','CM_DOC_DONACION_COMITE')


