from django.contrib import admin
from django.urls import path, include
from staff import views
from classain import views as clv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactFromView.as_view(), name='form'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),
    path('student/', clv.Student_Create_View.as_view(), name='student'),
    path('success/', clv.ThanksTemplateView.as_view(), name='success'),
    path('detail/<int:pk>', clv.StudentDetailView.as_view(), name='details'),
]
