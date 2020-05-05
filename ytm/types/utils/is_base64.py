'''
'''

import string
import re

def is_base64(data: str) -> bool:
    '''
    '''
    
    characters    = string.ascii_letters + string.digits + '+/'
    character_pad = '='

    if not re.match(f'^[{characters}]+{character_pad}*$', data):
        return False

    return len(data) % 4 == 0
