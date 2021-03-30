from django.contrib import admin
from staff.models import staff
# Register your models here.

@admin.register(staff)
class staffAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')