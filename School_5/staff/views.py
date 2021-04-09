from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        
        return HttpResponseRedirect('profile')
    else:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Account Created Successfully')
    
        else:
            fm = SignUpForm()

    return render(request, 'staff/signup.html',{'form':fm})


def user_login(request):
    if request.user.is_authenticated:
        
        return HttpResponseRedirect('profile')
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
                    return HttpResponseRedirect('profile')

        else:        
            fm = AuthenticationForm()

    return render(request, 'staff/userLogin.html',{'form':fm})


def user_profile(request):
    
    if request.user.is_authenticated:
        return render(request, 'staff/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('in')


def user_logout(request):

    logout(request)
    return HttpResponseRedirect('in')