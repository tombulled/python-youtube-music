'''
Module containing the parser: watch
'''

from .. import utils
from . import decorators
from . import cleansers

@decorators.enforce_parameters
@decorators.catch
def watch(data: dict):
    '''
    Parse data: Watch.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.next \
        (
            video_id    = 'HyHNuVaZJ-k',
        	playlist_id = 'RDCLAK5uy_kzInc7BXjYqbrGEiqW9fBhOZoroJvfsao',
        )
        >>>
        >>> parsed_data = ytm.parsers.watch(data)
        >>>
        >>> parsed_data['tracks'][0]['name']
        'Feel Good Inc'
        >>>
    '''

    assert data, 'No data to parse'

    if 'continuationContents' in data:
        playlist_renderer = utils.get \
        (
            data,
            'continuationContents',
            'playlistPanelContinuation',
        )
    else:
        playlist_renderer = utils.get \
        (
            data,
            'contents',
            'singleColumnMusicWatchNextResultsRenderer',
            'playlist',
            'playlistPanelRenderer',
        )

    assert playlist_renderer, 'No Playlist Renderer'

    tracks = utils.get \
    (
        playlist_renderer,
        'contents',
        default = (),
    )

    assert tracks, 'No Tracks'

    playlist_tracks = []

    for track in tracks:
        track = utils.first(track)

        assert track

        track_menu_items = utils.get \
        (
            track,
            'menu',
            'menuRenderer',
            'items',
            default = (),
        )

        track_menu = {}

        for menu_item in track_menu_items:
            menu_item = utils.first(menu_item)

            for key, val in menu_item.copy().items():
                if not key.startswith('default'):
                    continue

                new_key = key.replace('default', '')
                new_key = new_key[0].lower() + new_key[1:]

                menu_item[new_key] = menu_item.pop(key)

            menu_text = utils.get \
            (
                menu_item,
                'text',
                'runs',
                0,
                'text',
            )
            menu_icon = utils.get \
            (
                menu_item,
                'icon',
                'iconType',
            )
            menu_endpoint = utils.get \
            (
                menu_item,
                'navigationEndpoint',
            )

            if not menu_endpoint:
                continue

            menu_identifier = menu_text[0].lower() + menu_text.title()[1:].replace(' ', '') \
                if menu_text else None

            menu_item_data = \
            {
                'text':     menu_text,
                'icon':     menu_icon,
                'endpoint': menu_endpoint,
            }

            track_menu[menu_identifier] = menu_item_data

        track_watch_endpoint = utils.get \
        (
            track,
            'navigationEndpoint',
            'watchEndpoint',
        )
        track_radio_watch_endpoint = utils.get \
        (
            track_menu,
            'startRadio',
            'endpoint',
            'watchEndpoint',
        )
        track_artist_browse_endpoint = utils.get \
        (
            track_menu,
            'goToArtist',
            'endpoint',
            'browseEndpoint',
        )
        track_album_browse_endpoint = utils.get \
        (
            track_menu,
            'goToAlbum',
            'endpoint',
            'browseEndpoint',
        )

        track_selected = utils.get \
        (
            track,
            'selected',
        )
        track_music_video_type = utils.get \
        (
            track_watch_endpoint,
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )
        track_index = utils.get \
        (
            track_watch_endpoint,
            'index',
        )
        track_playlist_id = utils.get \
        (
            track_watch_endpoint,
            'playlistId',
        )
        track_params = utils.get \
        (
            track_watch_endpoint,
            'params',
        )
        track_id = utils.get \
        (
            track,
            'videoId',
        )
        track_name = utils.get \
        (
            track,
            'title',
            'runs',
            0,
            'text',
        )
        track_duration = utils.get \
        (
            track,
            'lengthText',
            'runs',
            0,
            'text',
            func = cleansers.iso_time,
        )
        track_artist_name = utils.get \
        (
            track,
            'shortBylineText',
            'runs',
            0,
            'text',
        )
        track_thumbnail = utils.get \
        (
            track,
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_radio_playlist_id = utils.get \
        (
            track_radio_watch_endpoint,
            'playlistId',
        )
        track_radio_params = utils.get \
        (
            track_radio_watch_endpoint,
            'params',
        )
        track_artist_id = utils.get \
        (
            track_artist_browse_endpoint,
            'browseId',
        )
        track_album_id = utils.get \
        (
            track_album_browse_endpoint,
            'browseId',
        )

        # return track ###

        track_data = \
        {
            'name':      track_name,
            'duration':  track_duration,
            'id':        track_id,
            'thumbnail': track_thumbnail,
            'album': \
            {
                'id': track_album_id,
            },
            'radio': \
            {
                'playlist_id': track_radio_playlist_id,
                'params':      track_radio_params, # Same for all
            },
            'artist': \
            {
                'id':   track_artist_id,
                'name': track_artist_name,
            },
        }

        playlist_tracks.append(track_data)

    playlist_name  = utils.get \
    (
        playlist_renderer,
        'title',
    )
    playlist_radio = utils.get \
    (
        playlist_renderer,
        'isInfinite',
    )
    playlist_id = utils.get \
    (
        playlist_renderer,
        'playlistId',
    )
    playlist_continuation = utils.get \
    (
        playlist_renderer,
        'continuations',
        0,
        'nextRadioContinuationData',
        'continuation',
    )
    playlist_total = utils.get \
    (
        playlist_renderer,
        'totalVideosText',
        'runs',
        0,
        'text',
        func = lambda total: int(total.strip().split(' ')[0]),
    )

    playlist_data = \
    {
        'id':           playlist_id,
        'name':         playlist_name,
        'continuation': playlist_continuation,
        'total':        playlist_total,
        'tracks':       playlist_tracks,
        'radio':        playlist_radio,
    }

    current_watch_endpoint = utils.get \
    (
        data,
        'currentVideoEndpoint',
        'watchEndpoint',
    )

    current_data = None

    if current_watch_endpoint is not None:
        current_metadata_renderer = utils.get \
        (
            data,
            'contents',
            'singleColumnMusicWatchNextResultsRenderer',
            'metadataScreen',
            'sectionListRenderer',
            'contents',
            0,
            'itemSectionRenderer',
            'contents',
            0,
            'musicWatchMetadataRenderer',
        )
        current_like_button_renderer = utils.get \
        (
            data,
            'playerOverlays',
            'playerOverlayRenderer',
            'actions',
            0,
            'likeButtonRenderer',
        )
        current_artist_runs = utils.get \
        (
            current_metadata_renderer,
            'byline',
            'runs',
            default = (),
        )[:-4:2]

        current_artists = []

        for current_artist_run in current_artist_runs:
            current_artist_name = utils.get \
            (
                current_artist_run,
                'text',
            )
            current_artist_id = utils.get \
            (
                current_artist_run,
                'navigationEndpoint',
                'browseEndpoint',
                'browseId',
            )

            current_artist_data = \
            {
                'name': current_artist_name,
                'id':   current_artist_id,
            }

            current_artists.append(current_artist_data)

        current_index = utils.get \
        (
            current_watch_endpoint,
            'index',
        )
        current_song_id = utils.get \
        (
            current_watch_endpoint,
            'videoId',
        )
        # current_artist_name = utils.get \
        # (
        #     current_metadata_renderer,
        #     'byline',
        #     'runs',
        #     0,
        #     'text',
        # )
        # current_artist_id = utils.get \
        # (
        #     current_metadata_renderer,
        #     'byline',
        #     'runs',
        #     0,
        #     'navigationEndpoint',
        #     'browseEndpoint',
        #     'browseId',
        # )
        current_year = utils.get \
        (
            current_metadata_renderer,
            'byline',
            'runs',
            -1,
            'text',
            func = int,
        )
        current_album_name = utils.get \
        (
            current_metadata_renderer,
            'albumName',
            'runs',
            0,
            'text',
        )
        current_album_id = utils.get \
        (
            current_metadata_renderer,
            'byline',
            'runs',
            -3,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        current_song_name = utils.get \
        (
            current_metadata_renderer,
            'title',
            'runs',
            0,
            'text',
        )
        current_views = utils.get \
        (
            current_metadata_renderer,
            'viewCountText',
            'runs',
            0,
            'text',
            func = lambda views: int(views.strip().split(' ')[0].replace(',', '')),
        )
        current_likes = utils.get \
        (
            current_like_button_renderer,
            'likeCount',
        )
        current_dislikes = utils.get \
        (
            current_like_button_renderer,
            'dislikeCount',
        )

        # Make this None if its a continuation
        current_data = \
        {
            'id':       current_song_id,
            'name':     current_song_name,
            'index':    current_index,
            'year':     current_year,
            'views':    current_views,
            'likes':    current_likes,
            'dislikes': current_dislikes,
            'artists':  current_artists,
            'album': \
            {
                'name': current_album_name,
                'id':   current_album_id,
            },
        }

    scraped = \
    {
        **playlist_data,
        'current': current_data,
    }

    return scraped
