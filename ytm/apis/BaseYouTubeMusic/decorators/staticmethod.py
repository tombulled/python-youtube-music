'''
'''

import functools
from typing import Callable, Any

def staticmethod(func: Callable) -> Callable:
    '''
    '''

    @functools.wraps(func)
    def wrapper(cls: object, *args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper
