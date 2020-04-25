import re

def is_float(string: str) -> bool:
    '''
    '''

    return re.match(r'^\d+\.\d+$', string.strip()) is not None
