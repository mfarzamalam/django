from django.shortcuts import render, HttpResponse

# Create your view here
sessionKey1 = 'name'
default = 'gesture'

def setSession(request):
        request.session[sessionKey1] = 'Farzam'
        # request.session.set_expiry(60)

        return render(request, 'staff/setSession.html')


def getSession(mimba):
        if sessionKey1 in mimba.session:
                name = mimba.session['name']
                        # Or
                # name = mimba.session.get(sessionKey1, default=default)
                keys = mimba.session.keys()
                items = mimba.session.items()
                # age = mimba.session.setdefault('age', '21')

                        # Reset the session expiry age
                mimba.session.modified = True

                
                return render(mimba, 'staff/getSession.html', {'name':name, 'keys':keys, 'items':items})
        else:
                return HttpResponse('Your Session is expired')

def deleteSession(delta):
        # if sessionKey1 in delta.session:
        #         del delta.session[sessionKey1]
        
        # To delete session with the id key. Simply put dead drop
        delta.session.flush()
        delta.session.clear_expired()

        return render(delta, 'staff/deleteSession.html')