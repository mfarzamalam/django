from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('h', cache_page(30)(views.home)),
    path('h2', views.home),
    path('a',views.about),
]
