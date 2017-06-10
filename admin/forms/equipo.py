from django.forms import ModelForm
from django import forms
from ..model.equipo import equipo_model
from ..utils import error_messages
from ..model.tipoe import tipoe_model
from ..fields.fields import ExtFileField

class equipo_form(ModelForm):

      def __init__(self,*args,**kwargs):
          super(equipo_form, self).__init__(*args, **kwargs)
          self.fields['tipoe'].choices=[(r.TE_ID,r.TE_NOMBRE)for r in tipoe_model.objects.all()]

      EQ_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      EQ_NOMBRE=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})
      EQ_PRECIO=forms.DecimalField(
          max_digits=10,decimal_places=0,
          widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Valor','id':'equipos'}),
          required=False,error_messages={'required':error_messages.required(),
                                        'max_digits':error_messages.max_message(10)})

      EQ_ESTADO=forms.BooleanField(
          required=False,
          widget=forms.CheckboxInput(attrs={'id':'firmado'}))



      tipoe=forms.ChoiceField(
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)

      EQ_DOC_CONTRATO=ExtFileField(
                                required=False,
                                ext_whitelist=['.doc','.docx','.pdf'])

      class Meta:
          model=equipo_model
          fields=('EQ_ID','EQ_NOMBRE','EQ_PRECIO','EQ_ESTADO')