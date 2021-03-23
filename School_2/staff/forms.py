from django.core import validators
from django import forms

def starts_with_s(value):
    letter = "q"
    if value[0].lower() != letter:
        raise forms.ValidationError('Name should start with '+letter.upper())

class staffRegister(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    # name2 = forms.CharField(validators=[starts_with_s])
    password = forms.CharField(widget=forms.PasswordInput)
    rePassword = forms.CharField( label='Re-enter Password',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['rePassword']

        if p1 != p2:
            raise forms.ValidationError("Password doesnot match")