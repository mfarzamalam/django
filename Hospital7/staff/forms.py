from django import forms

class RegisterStaff(forms.Form):
    name = forms.CharField(initial='your name', help_text='only 30 charaters allowed')
    email = forms.EmailField()
    password = forms.CharField()
    address = forms.CharField()