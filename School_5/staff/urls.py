from django.urls import path
from . import views

urlpatterns = [
    path('up',views.sign_up, name='signup'),
    path('in',views.user_login, name='login'),
    path('profile',views.user_profile),
    path('logout',views.user_logout, name='logout')
]   