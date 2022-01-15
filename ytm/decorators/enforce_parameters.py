'''
Module containing the decorator: enforce_parameters
'''

from ._enforce import _enforce
import functools
from typing import Callable, Any

def enforce_parameters(func: Callable) -> Callable:
    '''
    Enforce function argument types as specified by the functions type hints.

    Args:
        func: Function to decorate

    Returns:
        Decorated func.

    Example:
        >>> @enforce_parameters
        def foo(x: int) -> bool:
        	return 'not a bool'

        >>> # Acceptable
        >>> foo(1)
        'not a bool'
        >>>
        >>> # Not acceptable
        >>> foo('a')
        TypeError: Expected argument 'x' to be of type 'int' not 'str'
        >>>
    '''

    @_enforce \
    (
        parameters   = True,
        return_value = False,
    )
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        '''
        Wrap func to enforce argument types

        Args:
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            The wrapped functions return value
        '''

        return func(*args, **kwargs)

    return wrapper
