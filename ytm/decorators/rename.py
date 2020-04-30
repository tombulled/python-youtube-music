'''
Module containing the decorator: rename
'''

from typing import Callable
from ._set_attrs import _set_attrs

def rename(name: str) -> Callable:
    '''
    Decorator to rename a functions __name__ attribute.

    Args:
        name: New function name

    Returns:
        The function renaming decorator

    Example:
        >>> @rename('NEW_NAME')
        def foo():
        	pass

        >>> foo.__name__
        'NEW_NAME'
        >>>
    '''

    return _set_attrs({'__name__': name})
