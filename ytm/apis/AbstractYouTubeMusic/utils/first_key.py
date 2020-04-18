'''
'''

from typing import Any

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def first_key(dictionary: dict, default: Any = None) -> Any:
    '''
    '''

    return dictionary[list(dictionary)[0]] \
        if dictionary else default
