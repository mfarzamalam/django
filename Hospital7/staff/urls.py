from django.urls import path
from . import views

urlpatterns = [
    path('rs',views.showRegisterStaff),
]