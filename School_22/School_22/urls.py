from django.contrib import admin
from django.urls import path, include
from staff import views
from classain import views as clv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactFromView.as_view(), name='form'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),

        # ADD
    path('student/', clv.Student_Create_View.as_view(), name='student'),
    path('success/', clv.ThanksTemplateView.as_view(), name='success'),
    path('detail/<int:pk>', clv.StudentDetailView.as_view(), name='details'),

        # UPDATE
    path('update/<int:pk>', clv.Student_Update_View.as_view(), name='updates'),
    path('updatedSuccess/', clv.UpdateTemplateView.as_view(), name='updatedSuccess'),
    
        # DELETE
    path('delete/<int:pk>', clv.Student_Delete_View.as_view(), name='delete'),
]
