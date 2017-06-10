from django.forms import ModelForm
from django import forms
from ..model.repuestos import repuesto_model
from ..utils import error_messages
from ..repositories.marcas import marcas_repositoy
from ..repositories.proveedor import proveedor_repository
from ..repositories.tipoc import tipoc_repository


class repuesto_form(ModelForm):

      def __init__(self,*args,**kwargs):
          rs1=marcas_repositoy()
          rs2=proveedor_repository()
          rs3=tipoc_repository()

          super(repuesto_form, self).__init__(*args, **kwargs)
          self.fields['tipoc'].choices=rs3.all_for_select()
          self.fields['marcas'].choices=rs1.all_for_select()
          self.fields['proveedores'].choices=rs2.all_for_select2()


      RE_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      RE_NOMBRE=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})

      RE_PRECIO=forms.DecimalField(
          max_digits=9,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad Tiendas','id':'tiendas'}),
          required=True,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(9)})

      tipoc=forms.ChoiceField(
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)

      marcas=forms.ChoiceField(
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)

      proveedores=forms.ChoiceField(
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)
      class Meta:
          model=repuesto_model
          fields=('RE_ID','RE_NOMBRE','RE_PRECIO')