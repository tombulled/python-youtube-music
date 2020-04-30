'''
Module containing the utility function: filter
'''

from typing import Callable, Iterable

def filter \
        (
            iterable: Iterable,
            func:     Callable = None,
        ) -> Iterable:
    '''
    Filter an iterable.

    Return an iterable containing those items of iterable for which func(item)
    or func(key, item), depending on the iterable type, are true.

    Args:
        iterable: An iterable to filter
            Example: {'a': 1, 'b': None} or [1, None, 3, 4]
        func: A function to filter items by
            Note: If the iterable *is* a dictionary, the function signature
                is func(key: Any, item: Any) -> bool
            Note: If the iterable is *not* a dictionary, the function signature
                is func(item: Any) -> bool
            Example: lambda item: item is not None
    Returns:
        If isinstance(iterable, dict):
            Returns dict
        Else:
            Returns list
    Example:
        If isinstance(iterable, dict):
            >>> data = {'a': 1, 'b': None, 'c': 3}
            >>> filter(data, func = lambda key, val: val is not None)
            {'a': 1, 'c': 3}
            >>>
        Else:
            >>> data = [1, None, 3]
            >>> filter(data, func = lambda val: val is not None)
            [1, 3]
            >>>
    '''

    if isinstance(iterable, dict):
        if not func:
            func = lambda key, val: bool(val)

        return \
        {
            key: val
            for key, val in iterable.items()
            if func(key, val)
        }
    else:
        if func is None:
            func = bool

        return \
        [
            val
            for val in iterable
            if func(val)
        ]
