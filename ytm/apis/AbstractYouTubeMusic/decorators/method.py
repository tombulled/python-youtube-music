'''
'''

import functools
from typing import Callable, Any
from .catch import catch
from .... import decorators

def method(parser: Callable = None) -> Callable:
    if not parser:
        parser = lambda data: data

    def decorator(func: Callable) -> Callable:
        @decorators.enforce_return_value
        @decorators.parse(parser)
        @catch
        @decorators.enforce_parameters
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator
