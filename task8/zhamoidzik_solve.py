def cached(func):
    results = dict()

    def wrapped(*args, **kwargs):
        key = str(sorted(args) + sorted(kwargs.items()))
        if key in results.keys():
            print('still got it')
            return results[key]
        results[key] = func(*args, **kwargs)
        print(results[key])
    return wrapped


@cached
def por(a, b, c):
    return a * b * c


