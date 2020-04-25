'''
'''

from typing import Any

def first(iterable, default: Any = None) -> Any:
    '''
    '''

    if not iterable:
        iterable = (default,)

    if isinstance(iterable, dict):
        iterable = iterable.values()

    return next(item for item in iterable)
