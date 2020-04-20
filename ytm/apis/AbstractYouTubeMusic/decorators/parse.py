'''
'''

import functools
from typing import Callable, Any

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def parse(parser: Callable) -> Callable:
    '''
    '''

    def decorator(func: Callable) -> Callable:
        '''
        '''

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            '''
            '''

            return parser(func(*args, **kwargs))

        return wrapper

    return decorator
