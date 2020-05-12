'''
Module containing the utility function: is_base64
'''

import string
import re

def is_base64(data: str) -> bool:
    '''
    Check whether some data is a valid base64 string.

    The data is valid base64 if its length is a multiple of 4, has only been
    padded with the '=' character and contains only ascii letters, digits or
    the '+' character.

    Args:
        data: Data to check

    Returns:
        Whether the data is a valid base64 string

    Example:
        >>> is_base64('foo')
        False
        >>> is_base64('foo=')
        True
        >>>
    '''

    characters    = string.ascii_letters + string.digits + '+/'
    character_pad = '='

    if not re.match(f'^[{characters}]+{character_pad}*$', data):
        return False

    return len(data) % 4 == 0
