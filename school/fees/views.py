from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def django_fees(request):
    return render(request, 'feesD.html')

def python_fees(request):
    return render(request, 'feesP.html')