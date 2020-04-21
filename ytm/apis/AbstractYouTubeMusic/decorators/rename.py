'''
'''

import functools
from typing import Callable, Any

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def rename(name: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            return func(*args, **kwargs)

        wrapper.__name__ = name

        return wrapper

    return decorator
