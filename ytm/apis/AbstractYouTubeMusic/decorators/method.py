'''
Module containing the decorator: method
'''

import functools
from typing import Callable, Any
from .catch import catch
from .... import decorators

def method(parser: Callable = None) -> Callable:
    '''
    Returns a decorator linking a method to a parser.

    Returns a decorator which will perform the following:
        * Enforce return value type
        * Enforce argument types
        * Catch and re-raise exceptions

    Args:
        parser: Method parser function

    Returns:
        Method decorator

    Example:
        >>> def my_parser(data):
        	return data['key']

        >>>
        >>> @method(my_parser)
        def my_method(x: int) -> str:
        	return {'key': str(x)}

        >>>
        >>> # Acceptable
        >>> my_method(1)
        '1'
        >>>
        >>> # Unacceptable
        >>> my_method('a')
        MethodError: my_method() encountered an error: Expected argument 'x' to be of type 'int' not 'str'
        >>>
    '''

    if not parser:
        parser = lambda data: data

    def decorator(func: Callable) -> Callable:
        '''
        Decorate func as a method linked to a previously specified parser.

        Args:
            func: Function to decorate

        Returns:
            Decorated func
        '''

        @decorators.enforce_return_value
        @decorators.parse(parser)
        @catch
        @decorators.enforce_parameters
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator
