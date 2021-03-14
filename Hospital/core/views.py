from django.shortcuts import render

# Create your views here.

def home_page(request):
    details = {
        'h':'Welcome to the Home Page',
    }

    return render(request, 'core/index.html', details)