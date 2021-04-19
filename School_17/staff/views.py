from django.shortcuts import render
from .models import Student
from datetime import date, time
from django.db.models import Avg, Sum, Min, Max, Count, Q

# Create your views here.
def home(request):
                ### Get all the name with 
        # data = Student.objects.filter(name__iexact='Wanda')
                
                ### column name contain the following letter 
        data = Student.objects.filter(name__contains='EE')

                ### column id contain the following numbers
        data = Student.objects.filter(id__in = [27, 28, 30, 29])

                ### column marks contain the following marks
        data = Student.objects.filter(marks__in = [78, 98])

                ### column marks contain the following marks with greater than sign
        data = Student.objects.filter(marks__gt = 80)

                ### column marks contain the following marks with less than sign
        data = Student.objects.filter(marks__lt = 80)
        
                ### column marks contain the following marks with greater than and equal too sign
        data = Student.objects.filter(marks__gte = 70)
        
                ### column marks contain the following marks with less than and equal too sign
        data = Student.objects.filter(marks__lte = 80)
        
                ### column name starts with the following letter
        data = Student.objects.filter(name__istartswith='a')
        
                ### column name ends with the following letter
        data = Student.objects.filter(name__endswith='a')
        
                ### column passing_date give the range of following date
        data = Student.objects.filter(passing_date__range=('2021-05-01','2021-05-10'))
        
                ### column admission_date give the exact following date
        data = Student.objects.filter(admission_date__date=date(2020,5,4))
        
                ### column admission_date give the date which is greater than
        data = Student.objects.filter(admission_date__date__gt=date(2020,5,4))
        
                ### column passing_date give the year which is exactly equal
        data = Student.objects.filter(passing_date__year=2020)
        
                ### column passing_date give the year which is greater than
        data = Student.objects.filter(passing_date__year__gt=2020)
        
                ### column passing_date give the year which is less than
        data = Student.objects.filter(passing_date__year__lt=2021)
        
                ### column passing_date give the month which is less than
        data = Student.objects.filter(passing_date__month__lt=5)
        
                ### column passing_date give the day which is exactly equal
        data = Student.objects.filter(passing_date__day=15)
        
                ### column passing_date give the week which is exactly equal
        data = Student.objects.filter(passing_date__week_day=7)
        
                ### column passing_date give the quarter which is exactly equal
        data = Student.objects.filter(passing_date__quarter=2)
        
                ### column admission_date give the time which is greater than
        data = Student.objects.filter(admission_date__time__gt=time(6,00))
        
                ### column admission_date give the hour which is greater than
        data = Student.objects.filter(admission_date__hour__gt=19)
        
                ### column admission_date give the minute which is greater than
        data = Student.objects.filter(admission_date__minute__gt=19)
        
                ### column admission_date give the second which is greater than
        data = Student.objects.filter(admission_date__second__gt=19)
        
                ### column rollNo give the true if there is any data. if not than False
        data = Student.objects.filter(rollNo__isnull=False)


                ### Aggregate Functions
        # average = Student.objects.all()
        # data = average.aggregate(Avg('marks'))
        # data = average.aggregate(Sum('marks'))
        # data = average.aggregate(Min('marks'))
        # data = average.aggregate(Max('marks'))
        # data = average.aggregate(Count('marks'))


                ### Q object for AND(&) , OR(|) and NOT(~)
        # data = Student.objects.filter( Q(id=32) & Q(rollNo=74))
        # data = Student.objects.filter( Q(id=32) | Q(rollNo=69))
        # data = Student.objects.filter( ~Q(id=32))

                ### LIMIT data coming into the template
        data = Student.objects.all()[:2]
        data = Student.objects.all()[5:10]
        data = Student.objects.all()[0:10:2]

        print(data)
        # print("query=",data.query)
        
        return render(request, 'staff/home.html', {'students':data})