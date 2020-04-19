'''
'''

import functools
from typing import Callable, Any

__decorator__ = __name__.split('.')[-1]
__all__  = (__decorator__,)

def staticmethod(func: Callable) -> Callable:
    '''
    '''

    @functools.wraps(func)
    def wrapper(cls: object, *args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper
