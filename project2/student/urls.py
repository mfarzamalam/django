from django.urls import path
from . import views             # dot represents current directory

urlpatterns = [
    path('students',views.the_student),
    path('quantity',views.student_quantity)
]