'''
'''

import functools
from typing import Callable, Any
from .. import exceptions

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def catch(method_name):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
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
