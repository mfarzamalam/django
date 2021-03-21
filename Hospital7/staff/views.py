from django.shortcuts import render
from .forms import RegisterStaff
# Create your views here.

def showRegisterStaff(request):
    rs = RegisterStaff()

    return render(request, 'staff/staffRegister.html', {'form':rs})