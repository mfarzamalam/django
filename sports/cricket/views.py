from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def play_cricket(request):
    tournament = {'round':'first'}

    return render(request, 'cricket/c1.html',tournament)