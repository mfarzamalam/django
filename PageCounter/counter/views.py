from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def home(request):
    count = request.session.get('count',0)
    newCount = count + 1
    request.session['count'] = newCount

    return render(request, 'counter/home.html', {'count': newCount})


def deleteSession(request):

        request.session.flush()

        return HttpResponseRedirect('/')