from django.shortcuts import render, HttpResponse
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
from .forms import StudentForm


# Create your views here.
# class Student_Create_View(CreateView):
#     model = Student
#     fields = ['name','email','age']
#     # success_url = '/success/'
#     # template_name = 'classain/sform.html'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'nameClass'})
#         # form.fields['password'].widget = forms.PasswordInput(attrs={'class':'passClass'})
#         return form

class Student_Create_View(CreateView):
    form_class = StudentForm
    template_name = 'classain/student_form.html'
    # success_url = '/success/'


class ThanksTemplateView(TemplateView):
    template_name = "classain/success.html"


class StudentDetailView(DetailView):
    model = Student