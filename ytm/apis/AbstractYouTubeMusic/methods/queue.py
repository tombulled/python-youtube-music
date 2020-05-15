'''
Module containing the method: queue
'''

from .. import decorators
from .... import parsers
from ....types import \
(
    Union,
    SongId,
    SongRadioId,
    AlbumPlaylistBrowseId,
    AlbumPlaylistId,
    AlbumRadioId,
    AlbumShuffleId,
    ArtistRadioId,
    ArtistShuffleId,
    PlaylistBrowseId,
    PlaylistId,
    PlaylistRadioId,
    PlaylistShuffleId,
)

@decorators.method(parsers.queue)
def queue \
        (
             self:        object,
            *song_ids:    SongId,
             playlist_id: Union \
             (
                SongRadioId,
                AlbumPlaylistBrowseId,
                AlbumPlaylistId,
                AlbumRadioId,
                AlbumShuffleId,
                ArtistRadioId,
                ArtistShuffleId,
                PlaylistBrowseId,
                PlaylistId,
                PlaylistRadioId,
                PlaylistShuffleId,
             ) = None,
        ) -> list:
    '''
    Fetch queue data.

    Returns up to 200 songs.

    Args:
         self: Class Instance
        *song_ids: Song Id to enqueue
         playlist_id: Playlist Id to enqueue

    Returns:
        List of songs in the queue

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.YouTubeMusic()
        >>>
        >>> queue = api.queue('Gz3-4UuMWjQ', 'Ye8Er8MtiLk')
        >>>
        >>> for song in queue:
        	print(song['artist']['name'], '-', song['name'])

        Amber Run - Amen
        Amber Run - Kites
        >>>
    '''

    if song_ids:
        return self._base.queue(*song_ids)
    elif playlist_id:
        playlist_id_map = \
        {
            AlbumPlaylistBrowseId: AlbumPlaylistId,
            PlaylistBrowseId:      PlaylistId,
        }

        playlist_id_type = type(playlist_id)

        if playlist_id_type in playlist_id_map:
            playlist_id = playlist_id_map[playlist_id_type](str(playlist_id))

        return self._base.queue(playlist_id = playlist_id)
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'song_ids\' or \'playlist_id\''
        )
