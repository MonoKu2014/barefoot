from django.forms import ModelForm
from django import forms
from ..utils import error_messages
from ..model.proveedor import proveedor_model
from barefoot import settings

class proveedor_form(ModelForm):
      PV_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      PV_RUT=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rut','id':'rut'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})

      PV_NOMBRE=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})

      PV_DIRECCION=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion','id':'direccion'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,80),
                          'max_length':error_messages.min_length_message(5,80)})

      PV_FONO=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono','id':'fono'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,20),
                          'max_length':error_messages.min_length_message(5,20)})

      PV_MAIL=forms.EmailField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Email','id':'email'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50),
                          'invalid': error_messages.email_message()})
      PV_FECHA=forms.DateField(
          input_formats=settings.DATE_INPUT_FORMATS,
          widget=forms.DateInput(attrs={'class':'form-control date-picker','placeholder':'Fecha','id':'fecha_proveedor'},format='%d-%m-%Y'),
          required=True,
          error_messages={'required':error_messages.required()})


      PV_VENTA=forms.DecimalField(
          max_digits=9,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Venta','id':'venta'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(9)})


      class Meta:
          model=proveedor_model
          fields=('PV_ID','PV_RUT','PV_NOMBRE','PV_DIRECCION','PV_FONO','PV_MAIL','PV_FECHA','PV_VENTA')