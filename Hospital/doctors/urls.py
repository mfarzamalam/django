from django.urls import path
from . import views

urlpatterns = [
    path('pod',views.raise_doctors_pay)
]
