from django.forms import ModelForm
from django import forms
from ..model.herramienta import herramienta_model
from ..utils import error_messages
from ..repositories.componente import componente_repository

class herramienta_form(ModelForm):

      def __init__(self, *args, **kwargs):
        super(herramienta_form, self).__init__(*args, **kwargs)
        rs1=componente_repository()
        self.fields['componentes'].choices=rs1.all_for_select()

      HR_ID=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      HR_NOMBRE=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})

      componentes=forms.ChoiceField(
                              widget=forms.Select(attrs={'class':'form-control'}),
                              required=True)
      class Meta:
          model=herramienta_model
          fields=('HR_ID','HR_NOMBRE')