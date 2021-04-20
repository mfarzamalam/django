from django.db import models
from django.contrib.auth.models import User

# Create your models here.

        ### One to One RelationShip
class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    page_name = models.CharField(max_length=100)
    page_category = models.CharField(max_length=100)
    page_publish_date = models.DateField()

class Like(Page):
    panna = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()


        ### Many to One RelationShip
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publish_date = models.DateField()


        ### Many to Many RelationShip
class Song(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

        ### To view all the singers using comprehension method
    def sing_by(self):
        return ", ".join([str(singer) for singer in self.user.all()])