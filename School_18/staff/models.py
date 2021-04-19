from django.db import models

# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class Student(Common):
    fees = models.IntegerField()
    date = None

class Teacher(Common):
    salary = models.IntegerField()

class Contractor(Common):
    date = models.DateTimeField()
    payment = models.IntegerField()


        ### Multi-table inheritance
class ExamCenter(models.Model):
    CenterName = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class EligibleStudent(ExamCenter):
    name = models.CharField(max_length=100)
    rollNo = models.IntegerField()