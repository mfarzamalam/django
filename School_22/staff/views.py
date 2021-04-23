from django.shortcuts import render, HttpResponse
from .forms import ContactForm, AboutForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.
class ContactFromView(FormView):
    
    template_name = 'staff/form.html'
    form_class = AboutForm
    success_url = '/thanks'

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['your_name'])
        print(form.cleaned_data['your_email'])
        print(form.cleaned_data['your_message'])

        return super().form_valid(form)


class ThanksTemplateView(TemplateView):

    template_name = 'staff/thanks.html'