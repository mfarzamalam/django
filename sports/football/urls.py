from django.urls import path
from . import views

urlpatterns = [
    path('f1',views.play_football),
    path('f2',views.check_student)
]