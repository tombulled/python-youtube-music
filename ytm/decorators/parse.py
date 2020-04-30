'''
Module containing the decorator: parse
'''

import functools
from typing import Callable, Any

def parse(parser: Callable) -> Callable:
    '''
    Returns a decorator used to parse a functions return value before
    it is returned.

    Args:
        parser: Function used to parse the decorated functions return value

    Returns:
        Function decorator

    Example:
        >>> @parse(int)
        def foo():
        	return '1'

        >>> foo()
        1
        >>>
    '''

    def decorator(func: Callable) -> Callable:
        '''
        Decorate func to parse its return value

        Args:
            func: Function to decorate

        Returns:
            The decorated func
        '''

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            '''
            Wrap func to parse its return value

            Args:
                *args: Function arguments
                **kwargs: Function keyword arguments

            Returns:
                The wrapped functions return value
            '''

            return parser(func(*args, **kwargs))

        return wrapper

    return decorator
