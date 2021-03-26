from django.shortcuts import render
from .forms import staffRegister
from .models import User

# Create your views here.
def showStaffData(request):
    if request.method == 'POST':
        showData = staffRegister(request.POST)
        if showData.is_valid():
            name = showData.cleaned_data['name2']
            email = showData.cleaned_data['email']
            password = showData.cleaned_data['password']

            reg = User(name=name, email=email, password=password)
            reg.save()
    else:
        showData = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':showData})