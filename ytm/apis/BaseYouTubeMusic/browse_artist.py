'''
'''

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def browse_artist(self: object, browse_id: str) -> dict:
    '''
    '''
    
    return self.browse \
    (
        browse_id = browse_id,
    )
