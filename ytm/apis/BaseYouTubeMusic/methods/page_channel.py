'''
'''

from .. import constants

def page_channel(self: object, channel: str) -> dict:
    '''
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_CHANNEL,
        channel,
    )
