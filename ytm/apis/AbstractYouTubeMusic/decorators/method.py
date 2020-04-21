'''
'''

import functools
from typing import Callable, Any
# from .enforce import enforce
from .enforce_return import enforce_return
from .enforce_parameters import enforce_parameters
from .rename import rename
from .parse import parse
from .catch import catch

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def method(name: str, parser: Callable = None) -> Callable:
    if not parser:
        parser = lambda data: data

    def decorator(func: Callable) -> Callable:
        @enforce_return
        @parse(parser)
        @catch(name)
        @enforce_parameters
        @rename(name)
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator
