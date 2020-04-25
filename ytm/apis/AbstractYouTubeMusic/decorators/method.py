'''
'''

import functools
from typing import Callable, Any
# from . import enforce_return_value
# from . import enforce_parameters
# from .enforce_return import enforce_return
# from .enforce_parameters import enforce_parameters
# from .rename import rename
# from .parse import parse
from .catch import catch
# from . import parse
# from . import catch
from .... import decorators

def method(parser: Callable = None) -> Callable:
    if not parser:
        parser = lambda data: data

    def decorator(func: Callable) -> Callable:
        @decorators.enforce_return_value
        @decorators.parse(parser)
        @catch
        @decorators.enforce_parameters
        # @rename(name)
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator
