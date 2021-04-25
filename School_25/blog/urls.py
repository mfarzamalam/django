from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.ShowAllPost),
    path('view2/', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetalView.as_view(), name='post')
]
