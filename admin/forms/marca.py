from django.forms import ModelForm
from django import forms
from ..model.marca import marca_model
from ..utils import error_messages

class marca_form(ModelForm):
      id=forms.IntegerField(widget = forms.HiddenInput(),required=False)
      nombre=forms.CharField(
          min_length=5,max_length=50,
          widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','id':'nombre'}),
          required=True,
          error_messages={'required':error_messages.required(),
                          'min_length':error_messages.min_length_message(5,50),
                          'max_length':error_messages.min_length_message(5,50)})
      class Meta:
          model=marca_model
          fields=('id','nombre')