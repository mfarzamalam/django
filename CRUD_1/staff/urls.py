from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_and_read),
    path('delete/<int:did>/', views.delete_data, name="deleteData"),
    path('edit/<int:eid>/', views.update_and_edit, name="editData")
]
