from django.shortcuts import render
from .forms import RegisterStaff
# Create your views here.

def showRegisterStaff(request):
    rs = RegisterStaff()
    rs1 = RegisterStaff(auto_id='some_%s')
    rs2 = RegisterStaff(auto_id=True)
    rs3 = RegisterStaff(auto_id=False)
    rs4 = RegisterStaff(auto_id=False, label_suffix='--')
    rs5 = RegisterStaff(auto_id=False, label_suffix='=', initial={ 'name':'firstname secondname', 'email':'some@mail.com' })
    
    rs.order_fields(field_order=['email','address'])
    
    return render(request, 'staff/staffRegister.html', {'form':rs})