from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student

    # Custom has a HIGH priority than default in any field

    template_name = 'staff/student_list.html'
    # template_name_suffix = '_list'
    ordering = ['name']
    # context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Python')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')

        return context


    def get_template_names(self):
        # if self.request.user.is_superuser:
        #     template_name = 'staff/admin.html'
        # elif self.request.user.is_staff:
        #     template_name = 'staff/staff.html'
        # else:
        #     template_name = self.template_name
        # return template_name


        if self.request.COOKIES['user'] == 'farzam':
            template_name = 'staff/farzam.html'
        else:
            template_name = self.template_name

        return template_name