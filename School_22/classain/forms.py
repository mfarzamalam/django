from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name","age","email")
        widgets = {'name':forms.TextInput(attrs={'class':'myNameClass Second',}),
                    'age':forms.TextInput(attrs={'class':'myAgeClass'})}