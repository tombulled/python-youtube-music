'''
'''

from collections.abc import Iterable
from typing import Any, Callable

def get \
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
            if isinstance(key, int) and key < 0:
                key += len(item)

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
