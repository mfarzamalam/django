from django.urls import path
from . import views

urlpatterns = [
    path('pon',views.nurse_on_leave)
]
