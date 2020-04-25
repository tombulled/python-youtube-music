'''
'''

from .. import constants

def page_playlist(self: object, list: str) -> dict:
    '''
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_PLAYLIST,
        params = \
        {
            'list': list,
        },
    )
