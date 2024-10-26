def universal_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('finished')
        return res

    return wrapper


@universal_decorator
def some_func(text):
    print(text)
    return text


some_func('print me')
