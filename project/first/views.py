from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome Home")
    
def learn_django(request):
    head = ' Hello django '

    return HttpResponse(head)

def learn_python(request):
    head = '<h1> Hello python </h1>'

    return HttpResponse(head)

def welcome_user(request):
    user = 'Groot'

    return HttpResponse(f'Welcome {user}')