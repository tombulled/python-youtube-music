'''
Module containing the decorator: enforce_return_value
'''

from ._enforce import _enforce
import functools
from typing import Callable, Any

def enforce_return_value(func: Callable) -> Callable:
    '''
    Enforce function return value type as specified by the functions type hints.

    Args:
        func: Function to decorate

    Returns:
        Decorated func.

    Example:
        >>> @enforce_return_value
        def foo(x) -> int:
        	return x

        >>> # Acceptable
        >>> foo(1 + 3)
        4
        >>>
        >>> # Not acceptable
        >>> foo('a')
        TypeError: Expected return value to be of type 'int' not 'str'
        >>>
    '''

    @_enforce \
    (
        parameters   = False,
        return_value = True,
    )
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        '''
        Wrap func to enforce return value type

        Args:
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            The wrapped functions return value
        '''

        return func(*args, **kwargs)

    return wrapper
