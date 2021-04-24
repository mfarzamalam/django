from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    # path("profile/", login_required(views.my_profile), name="profile"),
    # path("contact/", staff_member_required(views.ContactView.as_view()), name="contact"),
    
    path("profile/", views.my_profile, name="profile"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.my_about.as_view(), name="about"),
]
