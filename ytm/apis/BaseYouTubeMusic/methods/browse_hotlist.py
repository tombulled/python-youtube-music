'''
'''

from .. import constants

def browse_hotlist(self: object) -> dict:
    '''
    '''

    return self.browse \
    (
        browse_id = constants.BROWSE_ID_HOTLIST,
    )
