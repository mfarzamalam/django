from django import forms

class RegisterStaff(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    address = forms.CharField()