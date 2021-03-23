from django.urls import path
from . import views

urlpatterns = [
     path('r',views.showStaffData),
     path('s',views.success)
]
