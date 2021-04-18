from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollNo = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    passing_date = models.DateField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    teacherNum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=100)
    salary = models.IntegerField()
    join_date = models.DateField()