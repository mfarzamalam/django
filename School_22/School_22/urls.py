from django.contrib import admin
from django.urls import path, include
from staff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactFromView.as_view(), name='form'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),
]
