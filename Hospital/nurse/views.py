from django.shortcuts import render

# Create your views here.

def nurse_on_leave(request):
    details = {
        'num':3,
        'who':'Nurses'
    }

    return render(request, 'nurse/index.html', details)