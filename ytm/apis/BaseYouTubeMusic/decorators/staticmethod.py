import functools

def staticmethod(func):
    @functools.wraps(func)
    def wrapper(cls, *args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
