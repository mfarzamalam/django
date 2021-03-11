from django.urls import path
from . import views

urlpatterns = [
    path('c1',views.play_cricket)
]