def dec(func):
    def wrapper(first, second):
        res = None
        if first == second:
            res = func(first, second, '+')
        elif first > second:
            res = func(first, second, '-')
        elif first < second:
            res = func(first, second, '/')

        if first < 0 < second:
            res = func(first, second, '*')
        elif first > 0 > second:
            res = func(first, second, '*')
        return res

    return wrapper


@dec
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return 'Choose correct operation'


print(calc(-2, -3))
