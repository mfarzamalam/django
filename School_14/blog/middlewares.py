# def my_middleware(get_response):
#     print("This will run one time")

#     def my_new_function(request):
#         print("This will run just before view")

#         response = get_response(request)

#         print(" This will run after view")
#         return response

#     return my_new_function


# class MyMiddlewares:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("This will run one time")

#     def __call__(self, request):
#         print("This will run just before view")
#         response = self.get_response(request)
#         print(" This will run after view")
        
#         return response

from django.shortcuts import HttpResponse
        ### More than one middlewares ###
# class brotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("This brother will run one time")

#     def __call__(self, request):
#         print("This brother will run just before view")
#         response = self.get_response(request)
#         print(" This brother will run after view")
        
#         return response

# class fatherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("This father will run one time")

#     def __call__(self, request):
#         print("This father will run just before view")
#         response = HttpResponse("Revert pal")
#         # response = self.get_response(request)
#         print(" This father will run after view")
        
#         return response

# class motherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("This mother will run one time")

#     def __call__(self, request):
#         print("This mother will run just before view")
#         response = self.get_response(request)
#         print(" This mother will run after view")
        
#         return response


        ### Middleware Hooks ###
# class MyProcessMiddlewares:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, *args, **kwargs):
#         print("process view before view")
#         # return HttpResponse("This is process View")
#         return None

# class MyExceptionMiddlewares:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         response = self.get_response(request)
#         return response

#     def process_exception(self, request, exception):
#         print("Exception Occured")
#         print(exception.__class__.__name__)
#         return HttpResponse(exception)
#         # return None

class MyTemplateResponseMiddlewares:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process Template response from Middleware")
        response.context_data['name'] = 'Farzam'

        return response