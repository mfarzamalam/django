from django.contrib import admin
from students.models import User
# Register your models here.

@admin.register(User)
class PrettyUser(admin.ModelAdmin):
    list_display = ('id','name','email','password')