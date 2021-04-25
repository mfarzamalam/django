from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='staff/home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='staff/dashboard.html'), name='dashboard'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),

    # path('logout/', auth_view.LogoutView.as_view(), name='logout'),

    path('changePass/', views.MyChangePassView.as_view() ,name='changePass'),
    path('changePassDone/', views.MyChangePassViewDone.as_view(), name='changePassDone'),
]
