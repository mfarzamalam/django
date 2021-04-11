from django.urls import path
from . import views

urlpatterns = [
    path('set',views.setCookie),
    path('get',views.getCookie),
    path('delete',views.deleteCookie),
]
