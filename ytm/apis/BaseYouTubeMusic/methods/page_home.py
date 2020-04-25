'''
'''

from .. import constants

def page_home(self: object) -> dict:
    '''
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_HOME,
    )
