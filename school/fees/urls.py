from django.urls import path
from . import views

urlpatterns = [
    path('pf',views.python_fees),
    path('df',views.django_fees)
]