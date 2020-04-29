'''
'''

from typing import Callable, Iterable

def filter \
        (
            iterable: Iterable,
            func:     Callable = None,
        ) -> dict:
    '''
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
