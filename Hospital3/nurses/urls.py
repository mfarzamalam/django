from django.urls import path
from . import views

urlpatterns = [
    path('n',views.nurse_required, name="nurses")
]
