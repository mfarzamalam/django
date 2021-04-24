from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

    # for staff member only user the decorator @staff_member_required

@login_required
def my_profile(request):
    return render(request, 'registration/profile.html')

@staff_member_required
def my_about(request):
    return render(request, 'registration/about.html')