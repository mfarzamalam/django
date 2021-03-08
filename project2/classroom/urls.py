from django.urls import path
from . import views             # dot represents the current directory

urlpatterns = [
    path('cquantity',views.classroom_quantity),
    path('cavailable',views.classroom_availabilty),
]