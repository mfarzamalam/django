from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showStudentData(request):
    if request.method == 'POST':
        ssd = StudentRegistration(request.POST)
        if ssd.is_valid():
            nm = ssd.cleaned_data['name']
            em = ssd.cleaned_data['email']
            ps = ssd.cleaned_data['password']
            
            register =User(name=nm , email=em, password=ps)
            register.save()
            
    else:
        ssd = StudentRegistration()

    return render(request, 'students/studentRegistration.html', {'form':ssd})