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