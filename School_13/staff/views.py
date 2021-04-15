from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

        # Set the value of cache if not available
def home(request):
    movie = cache.get('movie', 'has_expired')

    if movie == 'has_expired':
        cache.set('movie', 'Prestigue', 20)
        movie = cache.get('movie')

    return render(request, 'staff/home.html', {'movie':movie})


        # Get or set the value of cache with different versions
# def home(request):
#     movie = cache.get_or_set('fees', 500, 10, version=2)

#     return render(request, 'staff/home.html', {'movie':movie})


        # Set a dictionary as cache
# def home(request):
#     data = {'name':'Farzam', 'age':21, 'email':'mfarzamalam@gmail.com'}
#     cache.set_many(data, 5)
#     bloke = cache.get_many(data)

#     return render(request, 'staff/home.html', {'bloke':bloke})


        # Delete a particular cache with certain version
# def home(request):
#     cache.delete('fees', version=2)
#     return render(request, 'staff/home.html')


        # Set cache and increase and decrease the value
# def home(request):
#     cache.set('roll', 101, 40)
#     receiveValue = cache.get('roll')
#     print("Original Value:",receiveValue)
    
#     decreaseValue = cache.decr('roll', delta=2)
#     print("Increase value:",decreaseValue)

#     increaseValue = cache.incr('roll', delta=5)
#     print("Decrease value:",increaseValue)

#     return render(request, 'staff/home.html')


        # Clear all the cache 
# def home(request):
#     cache.clear()
#     return render(request, 'staff/home.html')