from django import forms

class RegisterStaff(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.HiddenInput())
    text = forms.CharField(widget=forms.Textarea())
    checkbox = forms.CharField(widget=forms.CheckboxInput())
    File = forms.CharField(widget=forms.FileInput())
    Name_with_attrs = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1'}))