from django import forms
from ..utils import error_messages

class login_form(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=50,required=True,min_length=5,
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required':error_messages.required(),
                                              'min_length':error_messages.min_length_message(5,50),
                                              'max_length':error_messages.min_length_message(5,50)})
    password=forms.CharField(label='Password',max_length=50,required=True,min_length=5,
                             widget=forms.PasswordInput(attrs={'class':'form-control'}),
                             error_messages={'required':error_messages.required(),
                                              'min_length':error_messages.min_length_message(5,50),
                                              'max_length':error_messages.min_length_message(5,50)})