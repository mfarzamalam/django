from django import forms

class staffRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()