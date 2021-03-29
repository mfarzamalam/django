from django.contrib import admin
from django.urls import path, include
from staff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staff.urls')),
    path('staffDetail/', include('staff.urls'))
]
