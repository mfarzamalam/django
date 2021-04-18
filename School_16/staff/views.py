from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
               ### Add a unique data so only one object return otherwise it'll give error
        # data = Student.objects.get(pk=1)

                ### Get the first data in the table
        # data = Student.objects.first()

                ### Get the first data according the the column
        # data = Student.objects.order_by('name').first()

                ### Get the last data in the table
        # data = Student.objects.last()

                ### Get the latest data added in the table
        # data = Student.objects.latest('passing_date')

                ### get the first data added in the table according to column
        # data = Student.objects.earliest('passing_date')

                ### if there is a data the true, otherwise false
        # data = Student.objects.all()
        # print("Data Exists:",data.exists())

                ### Create new data or check wether it's existed in the table or not
        # data = Student.objects.create(name='sameer', rollNo=115, city='Balochistan', marks=99, passing_date='2021-5-4')
        # data, created = Student.objects.get_or_create(name='sameer', rollNo=117, city='Balochistan', marks=99, passing_date='2021-4-14')
        # print("Created:",created)
        # print("Data:",data)

                ### Update the data if exist otherwise create new data
        # data = Student.objects.filter(rollNo=114).update(name='akmalo', city='Karachi')
        # data = Student.objects.filter(city='Karachi').update(name='kachry wala')
        # data, created = Student.objects.update_or_create(id=11, defaults={'name':'asghar','rollNo':'109', 'city':'Balochistan', 'marks':'89', 'passing_date':'2021-5-4'})
        # print("Created:",created)

                ### Create the data in bulk
        # objs = [
        #         Student(name='sallo', rollNo=52, city='Balochistan', marks=99, passing_date='2021-5-4'),
        #         Student(name='saleem', rollNo=53, city='Lahore', marks=98, passing_date='2021-5-4'),
        #         Student(name='saqib', rollNo=54, city='Balochistan', marks=78, passing_date='2021-5-4'),
        # ]
        # data = Student.objects.bulk_create(objs)

                ### get all the data in bulk
        # data = Student.objects.in_bulk()
        # data = Student.objects.in_bulk([1,2,3,4,5])
        # print(data[2].city)

                ### delete the data in bulk
        # data = Student.objects.all().delete()
        # data = Student.objects.get(pk=1).delete()
        # data = Student.objects.filter(marks=5000).delete()

                ### Count all the data in the table
        data = Student.objects.all()
        print(data.count())
        
        return render(request, 'staff/home.html', {'student':data})