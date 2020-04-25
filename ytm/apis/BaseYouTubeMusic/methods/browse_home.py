'''
'''

from .. import constants

def browse_home(self: object) -> dict:
    '''
    '''

    return self.browse \
    (
        browse_id = constants.BROWSE_ID_HOME,
    )
