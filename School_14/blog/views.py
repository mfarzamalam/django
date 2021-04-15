from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):

    print(" I am home view")

    return HttpResponse("This is home page")