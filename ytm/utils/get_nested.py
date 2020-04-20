'''
'''

from collections.abc import Iterable
from typing import Any, Callable

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def get_nested \
        (
            iterable: Iterable,
            *keys:    Any,
            default:  Any      = None,
            func:     Callable = None,
        ) -> Any:
    '''
    '''

    if not isinstance(iterable, Iterable) \
            or not iterable \
            or not keys:
        return default

    item = iterable

    for key in keys:
        if not isinstance(item, dict):
            item = dict(enumerate(item))

        if key not in item:
            return default

        item = item[key]

    if func:
        try:
            item = func(item)
        except:
            item = default

    return item
