from django.forms import ModelForm
from django import forms
from ..model.usuario import usuario_model
from ..utils import error_messages
from ..repositories.rol import rol_repositoy
from ..repositories.pais import pais_repository

class usuario_form(ModelForm):


      def __init__(self, *args, **kwargs):

        rs1=rol_repositoy()
        rs2=pais_repository()

        super(usuario_form, self).__init__(*args, **kwargs)
        self.fields['paises'].choices=rs2.all_for_select()
        self.fields['roles'].choices=rs1.all_for_select()


      id=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      nombre=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'txt_nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})
      apellido=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'apellidos','id':'apellido'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'min_length':error_messages.min_length_message(5,50),
                                        'max_length':error_messages.min_length_message(5,50)})

      usuario=forms.CharField(min_length=5,max_length=50,
                              widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Usuario'}),
                              required=True,error_messages={'required':error_messages.required(),
                                                            'min_length':error_messages.min_length_message(5,50),
                                                            'max_length':error_messages.min_length_message(5,50)})
      password=forms.CharField(min_length=5,max_length=50,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
                               required=True,error_messages={'required':error_messages.required(),
                                                             'min_length':error_messages.min_length_message(5,50),
                                                             'max_length':error_messages.min_length_message(5,50)})

      email=forms.CharField(
          min_length=8,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','id':'txt_email'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(8,50),
                          'max_length':error_messages.min_length_message(8,50)})

      roles=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)

      paises=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),
                               required=True)



      ing_precio_dia=forms.DecimalField(
          max_digits=10,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Precio','id':'ing_precio_dia'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(10)})



      class Meta:
          model=usuario_model
          fields=('id','nombre','apellido','usuario','password','email','ing_precio_dia')





