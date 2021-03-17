from django.db import models

# Create your models here.
class Patient(models.Model):
    p_id = models.IntegerField() 
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField(max_length=70)
    p_pass = models.CharField(max_length=100)