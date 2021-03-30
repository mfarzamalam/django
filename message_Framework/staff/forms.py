from django import forms
from staff.models import staff

class staffRegister(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['name','email','password']