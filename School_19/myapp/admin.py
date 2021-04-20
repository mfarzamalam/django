from django.contrib import admin
from .models import Page, Like

# Register your models here.
@admin.register(Page)
class Page_Admin(admin.ModelAdmin):
    list_display = ['page_name','page_category','page_publish_date','user']

@admin.register(Like)
class Like_Admin(admin.ModelAdmin):
    list_display = ['page_name','page_category','page_publish_date','user', 'likes']