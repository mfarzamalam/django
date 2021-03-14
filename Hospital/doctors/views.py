from django.shortcuts import render

# Create your views here.

def raise_doctors_pay(request):
    details = {
        'num':14,
        'who':'Doctors'
    }

    return render(request, 'doctors/index.html', details)