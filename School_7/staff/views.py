from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.models import User, Group

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        
        return HttpResponseRedirect('dashboard')
    else:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request, 'Account Created Successfully')
                user = fm.save()
                group = Group.objects.get(name='editor')
                user.groups.add(group)
    
        else:
            fm = SignUpForm()

    return render(request, 'staff/signup.html',{'form':fm})


def user_login(request):
    if request.user.is_authenticated:
        
        return HttpResponseRedirect('dashboard')
    else:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                userLogin = authenticate(username=uname, password=upass)

                if userLogin is not None:
                    login(request, userLogin)
                    messages.success(request, 'Login Successfully!')
                    return HttpResponseRedirect('dashboard')

        else:        
            fm = AuthenticationForm()

    return render(request, 'staff/userLogin.html',{'form':fm})


def user_dashboard(request):
    
    if request.user.is_authenticated:
        return render(request, 'staff/dashboard.html',{'name':request.user.first_name})

    else:
        return HttpResponseRedirect('login')


def user_logout(request):

    logout(request)
    return HttpResponseRedirect('login')