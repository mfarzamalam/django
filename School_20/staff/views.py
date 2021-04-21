from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm

# Create your views here.
class class_my_view(View):
    name = 'usama'

    def get(self,request):
        return HttpResponse('<h1> Class Based View - Get </h1>')
        # return HttpResponse(self.name)


class class_child_my_view(class_my_view):

    def get(self,request):
        # return HttpResponse(self.name)

        context = {'msg':'Your message is received via Class'}
        return render(request, 'staff/home.html', context)


class About_Class(View):
    def get(self,request):
        form = ContactForm()
        return render(request, 'staff/about.html', {'form':form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])

            return HttpResponse("Thank you for submitting the Form!")


class contact(View):
    template_name = ''

    def get(self, request):
        context = {'msg':'Welcome to the contact page'}

        return render(request, self.template_name, context)