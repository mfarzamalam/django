from django.shortcuts import render
from .forms import staffRegister
# Create your views here.
def register(request):
    if request.method == 'POST':
        fm = staffRegister(request.POST)

        if fm.is_valid():
            fm.save()
            fm = staffRegister()
    else:
        fm = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':fm})
