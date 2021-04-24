from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

    # for staff member only user the decorator @staff_member_required

# @login_required
# def my_profile(request):
#     return render(request, 'registration/profile.html')

# @staff_member_required
# def my_about(request):
#     return render(request, 'registration/about.html')


@method_decorator(login_required, name='dispatch')
class ContactView(TemplateView):
    template_name = 'registration/contact.html'

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)


def my_profile(request):
    return render(request, 'registration/profile.html')


class my_about(TemplateView):
    template_name = 'registration/about.html'

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)