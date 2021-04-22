from django.contrib import admin
from staff.models import create_read

# Register your models here.
@admin.register(create_read)
class all_staff(admin.ModelAdmin):
    list_display = ('id','name','email','password')