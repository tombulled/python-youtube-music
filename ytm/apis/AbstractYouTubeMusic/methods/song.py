'''
Module containing the method: song
'''

from .. import decorators
from .... import parsers
from ....types import SongId

@decorators.method(parsers.song)
def song(self: object, song_id: SongId) -> dict:
    '''
    Fetch Song data

    Args:
        self: Class Instance
        song_id: Song Id
            Example: '3G5Conn-b2o'

    Returns:
        Song data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.song('3G5Conn-b2o')
        >>>
        >>> data['name']
        'A Different Age'
        >>>
    '''

    # Accept a SongRadioId as well and just convert it?

    return self._base.video_info \
    (
        video_id = song_id,
    )
