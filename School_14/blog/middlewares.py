def my_middleware(get_response):
    print("This will run one time")

    def my_new_function(request):
        print("This will run just before view")

        response = get_response(request)

        print(" This will run after view")
        return response

    return my_new_function