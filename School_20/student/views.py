from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageTemplate(TemplateView):
    template_name = 'student/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'Farzam', 'age':22}

        return context