from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def django_fees(request):
    fees = 5000
    return HttpResponse("Django Fees :"+str(fees))

def python_fees(request):
    fees = 3000
    return HttpResponse("Python Fees :"+str(fees))