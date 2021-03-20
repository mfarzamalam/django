from django.contrib import admin
from room.models import Staff
# Register your models here.

@admin.register(Staff)

class PrettyStaff(admin.ModelAdmin):
    list_display = ('id','sid','sname','semail','spass')

# admin.site.register(Staff, PrettyStaff)