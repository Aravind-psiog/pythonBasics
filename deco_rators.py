def logger(fun):
    def wrapper(args, kwargs):
        print(args, kwargs)
        res = fun(args, kwargs)
        print(res)
        return res
    return wrapper


@logger
def add(a, b):
    res = a+b
    return res


@logger
def sub(a, b):
    res = a-b
    return res


add(1, 2)
sub(1, 2)
