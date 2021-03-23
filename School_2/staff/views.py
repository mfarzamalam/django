from django.shortcuts import render
from .forms import staffRegister

def showStaffData(request):
    showData = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':showData})