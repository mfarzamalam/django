from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('about/',views.about_page),
    path('d/',include('doctors.urls'))
]