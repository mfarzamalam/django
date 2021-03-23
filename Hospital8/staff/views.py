from django.shortcuts import render
from .forms import staffRegister

# Create your views here.
def showStaffData(request):
    if request.method == 'POST':
        showData = staffRegister(request.POST)
        if showData.is_valid():
            name = showData.cleaned_data['name']
            email = showData.cleaned_data['email']
            password = showData.cleaned_data['password']

            print("Name:",name)
            print("Email:",email)
            print("Password:",email)

            showData = staffRegister()
    else:
        showData = staffRegister()
        print("Empty Empty")

    return render(request, 'staff/staffRegister.html', {'form':showData})