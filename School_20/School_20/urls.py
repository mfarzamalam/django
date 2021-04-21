"""School_20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from staff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('c/',views.class_my_view.as_view(), name='c'),
    
    path('c/',views.class_my_view.as_view(name='farzam'), name='c'),
    
    path('sc/',views.class_child_my_view.as_view(), name='sc'),
    
    path('about/', views.About_Class.as_view(), name='contact'),

    path('contact/', views.contact.as_view(template_name='staff/contact.html'))


    


]
