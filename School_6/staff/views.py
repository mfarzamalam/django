from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.models import User

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
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                all_users = User.objects.all()

                if fm.is_valid():
                    messages.success(request,'Profile Updated For Admin')
                    fm.save()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                all_users = None

                if fm.is_valid():
                    messages.success(request,'Profile Updated For User')
                    fm.save()

        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                all_users = User.objects.all()

            else:
                fm = EditUserProfileForm(instance=request.user)
                all_users = None
        
        return render(request, 'staff/profile.html', {'name':request.user.first_name, 'form':fm, 'users':all_users})
    
    else:
        return HttpResponseRedirect('in')


def user_logout(request):

    logout(request)
    return HttpResponseRedirect('in')


def change_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('in')
    else:
        if request.method == 'POST':

            # change password with old password then use PasswordChangeForm
                                # OR
            # change password without old password then use SetPasswordForm
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('profile')
        
        else:
            fm = PasswordChangeForm(user=request.user)

    return render(request, 'staff/changePass.html', {'form':fm})


def admin_edit_user(request, id):
    if request.user.is_authenticated:
        single_user = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=single_user)

        return render(request, 'staff/details.html', {'form':fm})

    else:
        return HttpResponseRedirect('in')