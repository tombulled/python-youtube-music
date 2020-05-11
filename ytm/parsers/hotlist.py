'''
Module containing the parser: hotlist
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def hotlist(data: dict) -> list:
    '''
    Parse data: Hotlist.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_hotlist()
        >>>
        >>> parsed_data = ytm.parsers.hotlist(data)
        >>>
        >>> parsed_data[0]['name']
        'Me & You Together Song'
        >>>
    '''

    assert data, 'No data to parse'

    grid_items = utils.get \
    (
        data,
        'contents',
        'singleColumnBrowseResultsRenderer',
        'tabs',
        0,
        'tabRenderer',
        'content',
        'sectionListRenderer',
        'contents',
        0,
        'itemSectionRenderer',
        'contents',
        0,
        'gridRenderer',
        'items',
        default = (),
    )

    assert grid_items

    tracks = []

    for track in grid_items:
        track = utils.first(track)

        track_title = utils.get \
        (
            track,
            'title',
            'runs',
            0,
            'text',
        )
        track_views = utils.get \
        (
            track,
            'subtitle',
            'runs',
            -1,
            'text',
            func = lambda views: views.strip().split(' ')[0]
        )
        track_artist_id = utils.get \
        (
            track,
            'menu',
            'menuRenderer',
            'items',
            5,
            'menuNavigationItemRenderer',
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        track_thumbnail = utils.get \
        (
            track,
            'backgroundImage',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_id = utils.get \
        (
            track,
            'onTap',
            'watchEndpoint',
            'videoId',
        )
        track_music_video_type = utils.get \
        (
            track,
            'onTap',
            'watchEndpoint',
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )

        raw_track_artists = utils.get \
        (
            track,
            'subtitle',
            'runs',
            default = (),
        )[:-1:2]

        track_artists = []

        for track_artist in raw_track_artists:
            track_artist_title = utils.get \
            (
                track_artist,
                'text',
            )

            track_artists.append(track_artist_title)

        track_data = \
        {
            'id':        track_id,
            'name':     track_title,
            'views':     track_views,
            'artist': \
            {
                'id':    track_artist_id,
                'names': track_artists,
            },
            # 'artists':          track_artists,
            # 'artist_id':        track_artist_id,
            'thumbnail': track_thumbnail,
            # 'music_video_type': track_music_video_type,
        }

        tracks.append(track_data)

    return tracks
