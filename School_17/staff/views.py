from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
        data = Student.objects.all()
        
        print("query=",data.query)
        
        return render(request, 'staff/home.html', {'students':data})