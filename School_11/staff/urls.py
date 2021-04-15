from django.urls import path
from . import views

urlpatterns = [
    path('h',views.home),
    path('a',views.about),
]
