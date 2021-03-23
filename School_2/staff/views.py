from django.shortcuts import render
from .forms import staffRegister

# Create your views here.
def showStaffData(request):
    if request.method == 'POST':
        showData = staffRegister(request.POST)
        if showData.is_valid():
            name = showData.cleaned_data['name']
            email = showData.cleaned_data['email']

            print("Name:",name)
            print("Email:",email)

    else:
        showData = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':showData})