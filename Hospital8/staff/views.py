from django.shortcuts import render
from .forms import staffRegister

# Create your views here.
def showStaffData(request):
    sd = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':sd})