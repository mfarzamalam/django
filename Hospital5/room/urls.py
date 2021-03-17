from django.urls import path
from . import views

urlpatterns = [
    path('pview',views.Patient_info)
]
