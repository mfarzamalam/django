from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def class_teacher(request):
    return HttpResponse("There are two teacher in the classroom")

def my_teacher(request):
    return HttpResponse("Teacher is inside the class")