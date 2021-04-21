from django.shortcuts import render
from .models import User, Song, Like
# Create your views here.

# def show_user_data(request):
#     email = 'admin@gmail.com'
#     publish_date = '2021-04-20'
#     page_category = 'Programming'
#     song_duration = 9

#     data1 = User.objects.all()
#     data2 = User.objects.filter(email=email)
#     data3 = User.objects.filter(post__publish_date=publish_date)
#     data4 = User.objects.filter(page__page_category=page_category)
#     data5 = User.objects.filter(song__duration=song_duration)

#     context = {'data1':data1,  'data2':data2,'email':email,  'data3':data3,'publish_date':publish_date, 
#                 'data4':data4,'page_category':page_category,  'data5':data5,'song_duration':song_duration}

#     return render(request, 'myapp/data.html', context)


# def show_user_data(request):
#     username = 'Ali'
#     song_duration = 9

#     data1 = Song.objects.all()
#     data2 = Song.objects.filter(user__username=username)
#     data3 = Song.objects.filter(duration=song_duration)

#     context = {'data1':data1,  'data2':data2,'username':username,  'data3':data3,'song_duration':song_duration}

#     return render(request, 'myapp/data.html', context)


def show_user_data(request):

    data = Like.objects.filter(user__username='usama')

    return render(request, 'myapp/data.html', {'data':data})