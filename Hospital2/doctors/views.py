from django.shortcuts import render

# Create your views here.
def raise_doctor_pay(request):
    return render(request, 'doctors/doctorsInfo.html')

def decrease_doctor_pay(request):
    return render(request, 'doctors/doctorsInfo.html')