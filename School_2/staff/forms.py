from django.core import validators
from django import forms

class staffRegister(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name2 = forms.CharField(error_messages={'required':'Enter your Name'})
    email = forms.EmailField(error_messages={'required':'Enter your Email'}, min_length=10)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your Password'})