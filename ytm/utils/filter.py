'''
'''

from typing import Callable

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def filter \
        (
            iterable,
            func: Callable = None,
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
