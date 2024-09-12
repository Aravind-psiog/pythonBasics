a = [1, 2, 3, 4, 5]


def iterator():
    data = iter(a)
    print(next(data))
    print(next(data))


def generator():
    for d in a:
        yield d


generator()
