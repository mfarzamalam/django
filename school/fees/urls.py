from django.urls import path
from . import views

urlpatterns = [
    path('Pfees',views.django_fees),
    path('Dfees',views.python_fees)
]