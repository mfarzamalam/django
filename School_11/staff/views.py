from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(30)
def home(request):
    return render(request, 'staff/home.html')

# @cache_page(30)
def about(request):
    return render(request, 'staff/about.html')