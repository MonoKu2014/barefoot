from django.forms import ModelForm
from django import forms
from ..utils import error_messages
from ..model.usuario import usuario_model
from ..model.pais import pais_model
from ..model.ingeniero_solar import ingeniero_solar_model

class ingeniero_solar_form(ModelForm):
      ING_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      ING_NOMBRE=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})
      ING_PRECIO_DIA=forms.DecimalField(
          max_digits=10,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Precio','id':'equipos'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(10)})



      paises=forms.ChoiceField(choices=[(r.PA_ID,r.PA_NOMBRE)for r in pais_model.objects.all()],
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)

      usuarios=forms.ChoiceField(choices=[(r.id,r.nombre)for r in usuario_model.objects.all()],
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)
      class Meta:
          model=ingeniero_solar_model
          fields=('ING_ID','ING_NOMBRE','ING_PRECIO_DIA')