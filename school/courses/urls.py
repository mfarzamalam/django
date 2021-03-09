from django.urls import path
from . import views

urlpatterns = [
    path('ld',views.learn_django),
    path('lp',views.learn_python)
]