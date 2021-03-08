from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def classroom_quantity(request):
    return HttpResponse("There are seven classroom in the school")

def classroom_availabilty(request):
    return HttpResponse("Your classroom is ready to conquer")