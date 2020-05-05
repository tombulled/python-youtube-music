'''
'''

def patterns(*types: type, prepend: str = None) -> tuple:
    '''
    '''

    return tuple \
    (
        (prepend or '') + pattern
        for type in types
        for pattern in getattr(type, '_patterns', ())
    )
