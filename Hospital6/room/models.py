from django.db import models

# Create your models here.
class Staff(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    semail = models.CharField(max_length=100)
    spass = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.sname