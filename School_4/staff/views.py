from django.shortcuts import render

# Create your views here.
def home_page(request, check):
    print(check)
    
    return render(request, 'staff/home.html')

def show_one_detail(request, d_id):
    if d_id == 1:
        staff_detail = {'id':d_id, 'name':'Ali'}
    
    if d_id == 2:
        staff_detail = {'id':d_id, 'name':'Usama'}

    return render(request, 'staff/details.html', staff_detail)

def show_sub_detail(request, d_id, sub_id):
    if d_id == 1 and sub_id == 2:
        staff_detail = {'id':d_id, 'name':'Ali', 'sub_id':sub_id}
    
    if d_id == 1 and sub_id == 3:
        staff_detail = {'id':d_id, 'name':'Usama', 'sub_id':sub_id}

    return render(request, 'staff/details.html', staff_detail)