from django.shortcuts import render, HttpResponseRedirect
from .forms import studentRegistration
from .models import create_read
from django.views import View
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class create_and_read(TemplateView):
    template_name = 'staff/cr.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

        form = studentRegistration()
        all_data = create_read.objects.all()
        context = {'form':form, 'views':all_data}
        
        return context
    
    def post(self, request):
        cr = studentRegistration(request.POST)
        if cr.is_valid():
            cr.save()

        return HttpResponseRedirect('/')
        

class delete_data(RedirectView):
    url = '/'
    
    def get_redirect_url(self, *args, **kwargs):
        print("A",args)
        print("K",kwargs['did'])
        
        id = kwargs['did']
        create_read.objects.get(pk=id).delete()

        return super().get_redirect_url(*args, **kwargs)


class edit_and_update(View):

    def get(self, request, eid):
        single_data = create_read.objects.get(pk=eid)
        cr = studentRegistration(instance=single_data)
    
        return render(request, 'staff/u.html', {'update':cr})

    def post(self, request, eid):
        single_data = create_read.objects.get(pk=eid)
        cr = studentRegistration(request.POST, instance=single_data)
      
        if cr.is_valid():
            cr.save()

            return HttpResponseRedirect('/')