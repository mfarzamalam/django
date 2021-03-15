from django.shortcuts import render

# Create your views here.

def nurse_required(request):
    required_num = {'num':14}

    return render(request, 'nurses/index.html', required_num)