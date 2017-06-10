__author__ = 'victorfx'

from django.forms import ModelForm
from ..model.rol import rol_model
from django import forms
from ..utils import error_messages

class roles_form(ModelForm):
    id=forms.IntegerField(widget=forms.HiddenInput(),required=False)
    nombre=forms.CharField(
        min_length=5,max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Rol'}),
        required=True,
        error_messages={'required':error_messages.required(),
                        'min_length':error_messages.min_length_message(5,50),
                        'max_length':error_messages.min_length_message(5,50)})
    class Meta:
        model=rol_model
        fields=['id','nombre']
