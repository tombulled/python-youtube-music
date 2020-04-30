'''
Module containing the utility function: first
'''

from typing import Any, Iterable

def first(iterable: Iterable, default: Any = None) -> Any:
    '''
    Retrieve the first item from an iterable.

    Return the first item from an iterable, or the first value from
    from a dictionary

    Args:
        iterable: An iterable to retrieve the first item from
            Example: [1, 2, 3] or {'a': 1, 'b': 2}
        default: Default value for if the iterable is empty
            Example: -1

    Returns:
        The first item or value from the iterable

    Example:
        If isinstance(iterable, dict):
            >>> data = {'a': 1, 'b': 2}
            >>> first(data)
            1
            >>>
        Elif iterable:
            >>> data = [1, 2, 3]
            >>> first(data)
            1
            >>>
        Else:
            >>> data = []
            >>> first(data, default = 'Nothing there')
            'Nothing there'
            >>>
    '''

    if not iterable:
        iterable = (default,)

    if isinstance(iterable, dict):
        iterable = iterable.values()

    return next(item for item in iterable)
