from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setCookie(request):
    result = render(request, 'staff/setCookie.html')
    # result.set_cookie('name','farzam', expires=datetime.utcnow()+timedelta(days=2))
    result.set_signed_cookie('name','farzam',salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return result


def getCookie(request):
    # name = request.COOKIES['name']
            # Or (default is none if no key is available)
    # name = request.COOKIES.get('name')
            # Or (the other value is set when no key is available)
    # name = request.COOKIES.get('name', "Guest")
            # Or (for signed cookies)
    name = request.get_signed_cookie('name', default="Guest", salt='nm')

    return render(request, 'staff/getCookie.html', {'name':name})


def deleteCookie(request):
    result = render(request, 'staff/deleteCookie.html')
    result.delete_cookie('name')

    return result