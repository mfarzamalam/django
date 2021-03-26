from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showStudentData(request):
    if request.method == 'POST':
        ssd = StudentRegistration(request.POST)
        if ssd.is_valid():
            nm = ssd.cleaned_data['name']
            em = ssd.cleaned_data['email']
            ps = ssd.cleaned_data['password']
            
            print(nm)
            print(em)
            print(ps)
            
    else:
        ssd = StudentRegistration()

    return render(request, 'students/studentRegistration.html', {'form':ssd})