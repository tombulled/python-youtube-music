'''
Module containing the Id type: ArtistSongsPlaylistId
'''

from .. import base
from .. import constants

class ArtistSongsPlaylistId(base.Id):
    '''
    Id class: ArtistSongsPlaylistId

    Example:
        >>> id = ArtistSongsPlaylistId('VLOLAK5uy_mZabX2FA-77tDc8EpOSgCG-O-f37h7uFc')
        >>>
        >>> id
        <ArtistSongsPlaylistId('VLOLAK5uy_mZabX2FA-77tDc8EpOSgCG-O-f37h7uFc')>
        >>>
        >>> str(id)
        'VLOLAK5uy_mZabX2FA-77tDc8EpOSgCG-O-f37h7uFc'
        >>>
    '''

    _pattern: str = '^(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefix         = constants.PREFIX_ARTIST_PLAYLIST_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_PLAYLIST_ID,
    )
