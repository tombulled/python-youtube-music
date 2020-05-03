'''
Module containing the method: page_channel
'''

from .. import constants

def page_channel(self: object, channel: str) -> dict:
    '''
    Return page configuration data for: Channel.

    Page configuration data will contain player information and the initial
    endpoint

    Args:
        self: Class instance
        channel: Channel Id
            Example: 'UCN8aYfV4Em0pc0hxVXBTA-A'

    Returns:
        Channel page configuration data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.page_channel('UCN8aYfV4Em0pc0hxVXBTA-A')
        >>>
        >>> data['INITIAL_ENDPOINT']['browseEndpoint']['browseId']
        'UCN8aYfV4Em0pc0hxVXBTA-A'
        >>>
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_CHANNEL,
        channel,
    )
