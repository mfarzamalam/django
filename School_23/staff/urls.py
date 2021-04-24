from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.my_profile, name="profile"),
    path("about/", views.my_about, name="about"),
]
