''' xxx '''

import functools

def parse(parser):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resp = func(*args, **kwargs)
            parsed = parser(resp)

            return parsed

        return wrapper

    return decorator
