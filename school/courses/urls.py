from django.urls import path
from . import views

urlpattern = [
    path('learnDjango',views.learn_django),
    path('learnPython',views.learn_python)
]