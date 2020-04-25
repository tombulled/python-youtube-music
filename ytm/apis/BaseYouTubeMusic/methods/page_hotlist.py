'''
'''

from .. import constants

def page_hotlist(self: object) -> dict:
    '''
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_HOTLIST,
    )
