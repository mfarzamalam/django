from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','rollNo','city','marks','passing_date','admission_date']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','teacherNum','city','salary','join_date']