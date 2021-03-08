from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_class(request):
    return HttpResponse("My class from the view of teacher")