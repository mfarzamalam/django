from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def play_football(request):
    football = 'YES'
    team1 = 'barcelona'
    team2 = 'madrid'
    
    value = 'third'.upper()
    tournament = {
        'roundNum':value.title(),
        'football':football.lower(),
        't1':team1.title(),
        't2':team2.title(),
        }

    return render(request, 'football/f1.html', tournament)

def check_student(request):
    d_students = {
        'stu1':{'name':'ali','age':14},
        'stu2':{'name':'usama','age':18},
        'stu3':{'name':'akram','age':19},
        'stu4':{'name':'atif','age':21},
    }

    l_students = ['ali','ali2','ali3','ali4']

    all_students = {'d_students':d_students, 'l_students':l_students}

                                                # writing the keyword context is optional
    return render(request, 'football/f2.html',   context=all_students)