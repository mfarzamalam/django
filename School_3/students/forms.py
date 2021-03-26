from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Your Name','email':'Enter Email'}
        error_messages = {
            'name':{'required':'Name is importante'}
        }
        widgets = {'password':forms.PasswordInput, 
                    'name':forms.TextInput(attrs={'class':'cssOne', 'placeholder':'My name'})}