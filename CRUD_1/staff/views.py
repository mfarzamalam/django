from django.shortcuts import render, HttpResponseRedirect
from .forms import studentRegistration
from .models import create_read

# Create your views here.    
def create_and_read(request):
    if request.method == 'POST':
        cr = studentRegistration(request.POST)
        if cr.is_valid():
            # Use This
            # cr.save()
            
            # OR
            n = cr.cleaned_data['name']
            e = cr.cleaned_data['email']
            p = cr.cleaned_data['password']
            
            reg = create_read(name=n, email=e, password=p)
            reg.save()

            # to blank the form after entry of data
            cr = studentRegistration()

    else:
        cr = studentRegistration()

    all_data = create_read.objects.all()

    return render(request, 'staff/cr.html', {'form':cr, 'views':all_data})

def delete_data(request, did):
    if request.method == 'GET':
        single_data = create_read.objects.get(pk=did)
        single_data.delete()

        return HttpResponseRedirect('/')

def update_and_edit(request,eid):
    if request.method == 'POST':
        single_data = create_read.objects.get(pk=eid)
        cr = studentRegistration(request.POST, instance=single_data)
       
        if cr.is_valid():
            cr.save()
            return HttpResponseRedirect('/')

    else:
        single_data = create_read.objects.get(pk=eid)
        cr = studentRegistration(instance=single_data)

    return render(request, 'staff/u.html', {'update':cr})