from django.urls import path
from . import views

urlpatterns = [
    path('up',views.sign_up, name='signup'),
    path('in',views.user_login, name='login'),
    path('profile',views.user_profile, name='myProfile'),
    path('logout',views.user_logout, name='logout'),
    path('PassUpdate',views.change_password, name='PassUpdate')
]   