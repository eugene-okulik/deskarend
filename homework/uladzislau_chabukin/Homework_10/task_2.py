def decorator_1(func):
    def wrapper(text, count, *args, **kwargs):
        for _ in range(count):
            res = func(text, *args, **kwargs)
        return res

    return wrapper


def decorator_2(count):
    def func_decorator(func):
        def wrapper(text, *args, **kwargs):
            for _ in range(count):
                res = func(text, *args, **kwargs)
            return res

        return wrapper

    return func_decorator


@decorator_1
def some_func(text):
    print(text)
    return text


@decorator_2(count=2)
def some_func_2(text):
    print(text)
    return text


some_func('print me', count=2)

some_func_2('print me')
