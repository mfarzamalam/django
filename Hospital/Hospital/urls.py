from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', include('doctors.urls')),
    path('nurse/', include('nurse.urls')),
    path('', include('core.urls')),
]