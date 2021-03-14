from django.urls import path
from . import views

urlpatterns = [
    path('up',views.raise_doctor_pay),
    path('down',views.decrease_doctor_pay),
]
