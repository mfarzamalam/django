from django.shortcuts import render
from .forms import staffRegister
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        fm = staffRegister(request.POST)

        if fm.is_valid():
            fm.save()
            
            # Use this
            # messages.add_message(request, messages.INFO, 'Your Account has been created!')
            # Or
            messages.success(request, 'Your Account has been created')

            messages.debug(request, 'This is first Debug')
            print(messages.get_level(request))

            # Decrease the level or error messages to 10=='Debug'
            messages.set_level(request, messages.DEBUG)
            
            messages.debug(request, 'This is Second Debug')
            print(messages.get_level(request))

    else:
        fm = staffRegister()

    return render(request, 'staff/staffRegister.html', {'form':fm})
