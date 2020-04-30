'''
Module containing the decorator: _set_attrs
'''

from typing import Callable

def _set_attrs(attrs: dict) -> Callable:
    '''
    Update a class or functions attributes with attrs

    Args:
        attrs: Attributes to update the class or function with

    Returns:
        The attribute-setting decorator

    Example:
        >>> @_set_attrs({'__name__': 'NEW_NAME'})
        def foo(a, b):
        	return a + b

        >>>
        >>> foo.__name__
        'NEW_NAME'
        >>>
    '''

    def decorator(func: Callable) -> Callable:
        '''
        Decorate func to update its attributes as previously specified

        Args:
            func: Function to decorate

        Returns:
            The decorated func
        '''

        for key, val in attrs.items():
            setattr(func, key, val)

        return func

    return decorator
