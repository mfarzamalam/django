from django.shortcuts import render
from .forms import staffRegister

# Create your views here.
def showStaffData(request):
    if request.method == 'POST':
        showData = staffRegister(request.POST)
        if showData.is_valid():
            # name = showData.cleaned_data['name2']
            p1 = showData.cleaned_data['password']
            p2 = showData.cleaned_data['rePassword']

            # print("Name:",name)
            print("Password:",p1)
            print("Re-enter Password:",p2)

    else:
        showData = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':showData})