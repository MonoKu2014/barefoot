from django.forms import ModelForm
from django import forms
from ..model.taller_solar import taller_solar_model
from ..utils import error_messages

class taller_solar_form(ModelForm):
      TS_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      TS_LUGAR=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})

      TS_DIAS_USO_INGENIEROS=forms.IntegerField(
          required=True,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Dias Uso Ingenieros','id':'dias_ingenieros'}),
          error_messages={'required':error_messages.required()})

      TS_DIAS_USO_COMUNIDAD=forms.IntegerField(
          required=True,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Dias Uso Comunidad','id':'dias comunidad'}),
          error_messages={'required':error_messages.required()}
      )

      TS_DESCRIPCION=forms.CharField(
          required=True,
          min_length=5,max_length=99,
          widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripcion','id':'descripcion','rows':'4'}),
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,99),
                          'max_length':error_messages.min_length_message(5,99)
                          }
      )

      TS_HABILITADO=forms.BooleanField(
          required=False,
          widget=forms.CheckboxInput(attrs={'id':'habilitado'}))

      class Meta:
          model=taller_solar_model
          fields=('TS_ID','TS_LUGAR','TS_DIAS_USO_INGENIEROS','TS_DIAS_USO_COMUNIDAD','TS_DESCRIPCION','TS_HABILITADO')