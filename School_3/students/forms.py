from django.core import validators
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=100, min_length=5)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)