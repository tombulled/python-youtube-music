'''
Module containing the decorator: rename_module
'''

from typing import Callable
from ._set_attrs import _set_attrs

def rename_module(name: str) -> Callable:
    '''
    Decorator to rename a functions __module__ attribute.

    Args:
        name: New module name

    Returns:
        The module renaming decorator

    Example:
        >>> @rename_module('NEW_NAME')
        def foo():
        	pass

        >>> foo.__module__
        'NEW_NAME'
        >>>
    '''

    return _set_attrs({'__module__': name})
