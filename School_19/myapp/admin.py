from django.contrib import admin
from .models import Page, Like, Post, Song

# Register your models here.
@admin.register(Page)
class Page_Admin(admin.ModelAdmin):
    list_display = ['page_name','page_category','page_publish_date','user']

@admin.register(Like)
class Like_Admin(admin.ModelAdmin):
    list_display = ['page_name','page_category','page_publish_date','user', 'likes']


@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    list_display = ['id','user','title','category', 'publish_date']


@admin.register(Song)
class Song_Admin(admin.ModelAdmin):
    list_display = ['id','name','duration','sing_by']