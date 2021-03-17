from django.shortcuts import render
from room.models import Patient

# Create your views here.
def Patient_info(request):
    get_all = Patient.objects.all()
    get_one = Patient.objects.get(pk=3)      # Extracting only one data through pk(primary key)

    all_patient = {'p':get_all}

    return render(request, 'room/pview.html', all_patient)