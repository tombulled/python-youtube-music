'''
'''

import functools
from typing import Callable, Any
from .. import exceptions

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def catch(method_name):
    def decorator(func: Callable):
        # method = func.__module__.
        # print(func.__module__)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                resp = func(*args, **kwargs)
            except:
                resp = None

            if resp is None:
                raise exceptions.InvalidResponseError \
                (
                    f'Invalid response when parsing for method {repr(method_name)}',
                )

            return resp

        return wrapper

    return decorator
