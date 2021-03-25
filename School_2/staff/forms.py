from django.core import validators
from django import forms

def starts_with_s(value):
    letter = "q"
    if value[0].lower() != letter:
        raise forms.ValidationError('Name should start with '+letter.upper())

class staffRegister(forms.Form):
    error_css_class = 'error_css'
    required_css_class = 'require_css'

    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name2 = forms.CharField(error_messages={'required':'Enter your Name'})
    email = forms.EmailField(error_messages={'required':'Enter your Email'}, min_length=10)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your Password'})