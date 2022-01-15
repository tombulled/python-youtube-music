'''
Module containing the utility function: is_float
'''

import re

def is_float(string: str) -> bool:
    '''
    Check whether a string represents a float.

    The string must follow the format {number(s)}.{number(s)} to quality
    as a float

    Args:
        string: String to check
            Note: The string will be stripped

    Returns:
        Whether the string represents a float

    Example:
        >>> is_float('1.0')
        True
        >>> is_float('.0')
        False
        >>> is_float('1')
        False
        >>> is_float('a')
        False
        >>> is_float('123923.908908992    ')
        True
        >>>
    '''

    return re.match(r'^\d+\.\d+$', string.strip()) is not None
