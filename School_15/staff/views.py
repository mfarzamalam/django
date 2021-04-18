from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
# Create your views here.

def home(request):
            ### To retrieve all the data in table
    # all_student = Student.objects.all()


            ### To return specific colum with WHERE clause
    # all_student = Student.objects.filter(marks=32)


            ### Removing the data with specific column
    # all_student = Student.objects.exclude(marks=32)


            ### Ascending order with specific column, for descending use ('-')sign, for random use ('?')sign
    # all_student = Student.objects.order_by('city')
    # all_student = Student.objects.order_by('-city')
    # all_student = Student.objects.order_by('?')


            ### Order in reverse
    # all_student = Student.objects.order_by('id').reverse()[2:]


            ### All the data in the dictionary format
    # all_student = Student.objects.values()
    # all_student = Student.objects.values('name','city')


            ### All data in the tuple format
    # all_student = Student.objects.values_list()
    # all_student = Student.objects.values_list('id','name')
    # all_student = Student.objects.values_list('id','name', named=True)


            ### Define which database you're using
    # all_student = Student.objects.using('default')


            ### Data by day, week, month and year
    # all_student = Student.objects.dates('passing_date','week')


            ### UNION of two table, all data shown and common data once
    # all_student = Student.objects.values_list('id','name', named=True)
    # all_teacher = Teacher.objects.values_list('id','name', named=True)
    # data = all_teacher.union(all_student)
    # data = all_teacher.union(all_student, all=True)


            ### INTERSECTION of two table, only common data shown once
    # all_student = Student.objects.values_list('name', named=True)
    # all_teacher = Teacher.objects.values_list('name', named=True)
    # data = all_teacher.intersection(all_student)


      ### DIFFERENCE of two table, common data thrown out rest will shown
    # all_student = Student.objects.values_list('name', named=True)
    # all_teacher = Teacher.objects.values_list('name', named=True)
    # data = all_student.difference(all_teacher)


    ### AND operators
    # data = Student.objects.filter(id=2) & Student.objects.filter(name='farzam')
    # data = Student.objects.filter(id=2, name='farzam')
    # data = Student.objects.filter( Q(id=2) & Q(name='farzam'))


    ### OR operators
    # data = Student.objects.filter(id=2) | Student.objects.filter(name='farzama')
    data = Student.objects.filter( Q(id=2) | Q(name='farzam'))


    print(data)
    print("query =",data.query)

    return render(request, 'staff/home.html', {'students':data})