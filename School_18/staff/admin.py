from django.contrib import admin
from staff.models import Student, Teacher, Contractor

# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','name','age','fees']

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['id','name','age','date','salary']

@admin.register(Contractor)
class AdminContractor(admin.ModelAdmin):
    list_display = ['id','name','age','date','payment']