'''
Module containing the decorator: enforce
'''

from ._enforce import _enforce
import functools
from typing import Callable, Any

def enforce(func: Callable) -> Callable:
    '''
    Enforce function argument types and return value type as specified by the
    functions type hints.

    Args:
        func: Function to decorate

    Returns:
        Decorated func.

    Example:
        >>> @enforce
        def foo(x: int, func = str) -> str:
        	return func(x)

        >>>
        >>> # Arguments: Acceptable
        >>> foo(1)
        '1'
        >>> # Arguments: Unacceptable
        >>> foo('a')
        TypeError: Expected argument 'x' to be of type 'int' not 'str'
        >>>
        >>> # Return Value: Acceptable
        >>> foo(1, func = str)
        '1'
        >>> # Return Value: Unacceptable
        >>> foo(1, func = int)
        TypeError: Expected return value to be of type 'str' not 'int'
        >>>
    '''

    @_enforce \
    (
        parameters   = True,
        return_value = True,
    )
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        '''
        Wrap func to enforce argument and return value types

        Args:
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            The wrapped functions return value
        '''

        return func(*args, **kwargs)

    return wrapper
