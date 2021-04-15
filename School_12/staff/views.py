from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'staff/home.html')

# @cache_page(30)
def about(request):
    return render(request, 'staff/about.html')