'''
'''

import re

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def is_float(string: str) -> bool:
    '''
    '''

    return re.match(r'^\d+\.\d+$', string.strip()) is not None
