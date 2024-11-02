def logger_decorator(func):
    def decorated_func(*args, **kwargs):
        print("Function name:", func.__name__)
        if args and hasattr(args[0], func.__name__):
            print("Arguments:", tuple(args[1:]), kwargs)
        else:
            print("Arguments:", tuple(args), kwargs)
        result = func(*args, **kwargs)
        print("Return value:", result)
        return result

    return decorated_func
