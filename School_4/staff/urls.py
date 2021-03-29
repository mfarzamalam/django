from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, {'check':'OK'}, name="home" ),
    path('<int:d_id>/', views.show_one_detail, name="detail"),
    path('<int:d_id>/<int:sub_id>/', views.show_sub_detail, name="sub_detail")
]
