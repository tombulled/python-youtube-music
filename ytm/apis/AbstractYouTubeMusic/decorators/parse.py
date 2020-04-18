'''
'''

import functools
from typing import Callable, Any

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
