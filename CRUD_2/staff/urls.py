from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_and_read.as_view(), name="home"),
    path('delete/<int:did>/', views.delete_data.as_view(), name="deleteData"),
    path('edit/<int:eid>/', views.edit_and_update.as_view(), name="editData")
]
