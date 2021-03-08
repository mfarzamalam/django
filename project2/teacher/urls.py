from django.urls import path
from . import views             # dot represents current directory

urlpatterns = [
    path('classroom/',views.class_teacher),
    path('teacher/',views.my_teacher)
]