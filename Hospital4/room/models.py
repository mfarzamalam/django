from django.db import models

# Create your models here.
class Patient(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=100)
    pemail = models.EmailField(max_length=100)
    ppass = models.CharField(max_length=100)
    pcomment = models.CharField(max_length=50, default='No comments')