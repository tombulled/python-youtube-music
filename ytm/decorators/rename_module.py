'''
'''

from typing import Callable
from ._set_attrs import _set_attrs

def rename_module(name: str) -> Callable:
    '''
    '''
    
    return _set_attrs({'__module__': name})
