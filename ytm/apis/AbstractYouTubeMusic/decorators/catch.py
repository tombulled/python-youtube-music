'''
Module containing the decorator: catch
'''

import functools
from typing import Callable, Any
from .... import exceptions

def catch(func: Callable) -> Callable:
    '''
    Catch method errors and re-raise them appropriately.

    Methods can raise exceptions when something goes wrong,
    this decorator re-raises them as MethodError exceptions

    Args:
        func: Function to decorate

    Returns:
        Decorated func

    Raises:
        MethodError: The method encountered an error

    Example:
        >>> @catch
        def my_method(x):
        	assert isinstance(x, int), 'x was not an integer'


        >>> # Acceptable
        >>> my_method(1)
        >>>
        >>> # Unacceptable
        >>> my_method('a')
        MethodError: my_method() encountered an error: x was not an integer
        >>>
    '''

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        '''
        Wrap func to re-raise exceptions as method errors.

        Args:
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            The wrapped functions return value
        '''

        error_message = 'Unknown'

        try:
            return func(*args, **kwargs)
        except Exception as error:
            error_message = str(error)

        raise exceptions.MethodError \
        (
            f'{func.__name__}() encountered an error: {error_message}'
        )

    return wrapper
