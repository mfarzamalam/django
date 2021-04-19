from django.contrib import admin
from staff.models import Student, Teacher, Contractor, ExamCenter, EligibleStudent

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


@admin.register(ExamCenter)
class AdminExamCenter(admin.ModelAdmin):
    list_display = ['id','CenterName','city']

@admin.register(EligibleStudent)
class AdminEligibleStudent(admin.ModelAdmin):
    list_display = ['id','CenterName','city', 'name', 'rollNo']