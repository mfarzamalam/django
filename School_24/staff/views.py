from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm


# Create your views here.
class MyLoginView(LoginView):
    template_name='staff/login.html'
    authentication_form=LoginForm

class MyChangePassView(PasswordChangeView):
    template_name='staff/changePass.html'
    success_url='/changePassDone'

class MyChangePassViewDone(PasswordChangeDoneView):
    template_name='staff/changePassDone.html'

class MyLogoutView(LogoutView):
    template_name='staff/logout.html'