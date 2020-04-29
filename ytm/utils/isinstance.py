'''
'''

import builtins

def isinstance(object: object, class_: type) -> bool:
    '''
    '''

    return builtins.isinstance(object, class_) \
        or getattr(class_, '_validate', lambda object: False)(object)
