'''
'''

import functools
from typing import Callable, Any
from .... import exceptions

def catch(func: Callable):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        error_message = 'Unknown'

        try:
            return func(*args, **kwargs)
        except Exception as _error:
            error_message = str(_error)

        raise exceptions.MethodError \
        (
            f'{func.__name__}() encountered an error: {error_message}'
        )

    return wrapper
