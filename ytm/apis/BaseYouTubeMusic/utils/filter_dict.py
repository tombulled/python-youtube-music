'''
'''

from typing import Callable

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def filter_dict \
        (
            dictionary: dict,
            func: Callable[[str, str], dict] = None,
        ) -> dict:
    '''
    '''

    if func is None:
        func = lambda key, val: bool(val)

    return \
    {
        key: val
        for key, val in dictionary.items()
        if func(key, val)
    }
