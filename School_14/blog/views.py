from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

# def Home(request):
#     print(" I am home view")

#     return HttpResponse("This is home page")


# def home_exception(request):
#     print("This is exception view")
#     a = 10/0

#     return HttpResponse("This is from exception view")


def user_info(request):
    print("This is User Info view")
    context = {'name': 'Roheela'}

    return TemplateResponse(request, 'blog/home.html', context)