from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def student_quantity(request):
    return HttpResponse("There are 18 student inside the class")

def the_student(request):
    return HttpResponse("The students are inside the class")