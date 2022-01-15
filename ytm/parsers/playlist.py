'''
Module containing the parser: playlist
'''

from .. import utils
from . import decorators
from . import cleansers

@decorators.enforce_parameters
@decorators.catch
def playlist(data: dict) -> dict:
    '''
    Parse data: Playlist.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_playlist('VLRDCLAK5uy_kzInc7BXjYqbrGEiqW9fBhOZoroJvfsao')
        >>>
        >>> parsed_data = ytm.parsers.playlist(data)
        >>>
        >>> parsed_data['name']
        'Feel-Good 00s'
        >>>
    '''

    assert data, 'No data to parse'

    if 'continuationContents' in data:
        playlist_data = None

        data = utils.get \
        (
            data,
            'continuationContents',
            'musicPlaylistShelfContinuation',
        )

        continuation = utils.get \
        (
            data,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )
    else:
        music_detail_header_renderer = utils.get \
        (
            data,
            'header',
            'musicDetailHeaderRenderer',
        )
        music_playlist_shelf_renderer = utils.get \
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
            'musicPlaylistShelfRenderer',
        )
        playlist_menu_items = utils.get \
        (
            music_detail_header_renderer,
            'menu',
            'menuRenderer',
            'items',
            default = (),
        )
        playlist_menu_button_items = utils.get \
        (
            music_detail_header_renderer,
            'menu',
            'menuRenderer',
            'topLevelButtons',
            default = (),
        )

        playlist_menu = {}

        for menu_item in playlist_menu_items + playlist_menu_button_items:
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

            playlist_menu[menu_identifier] = menu_item_data

        assert music_detail_header_renderer
        assert music_playlist_shelf_renderer

        # return utils.get \
        # (
        #     music_detail_header_renderer,
        #     'subtitle',
        #     'runs',
        #     2,
        # )
        # return music_playlist_shelf_renderer
        # return data
        # return playlist_menu

        playlist_radio_playlist_id = utils.get \
        (
            playlist_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'playlistId',
        )
        playlist_radio_params = utils.get \
        (
            playlist_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'params',
        )
        playlist_shuffle_playlist_id = utils.get \
        (
            playlist_menu,
            'shuffle',
            'endpoint',
            'watchPlaylistEndpoint',
            'playlistId',
        )
        playlist_shuffle_params = utils.get \
        (
            playlist_menu,
            'shuffle',
            'endpoint',
            'watchPlaylistEndpoint',
            'params',
        )
        playlist_title = utils.get \
        (
            music_detail_header_renderer,
            'title',
            'runs',
            0,
            'text',
        )
        playlist_type = utils.get \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            0,
            'text',
        )
        playlist_artist_name = utils.get \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            2,
            'text',
        )
        playlist_artist_id = utils.get \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            2,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        playlist_year = utils.get \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            4,
            'text',
            func = int,
        )
        playlist_thumbnail = utils.get \
        (
            music_detail_header_renderer,
            'thumbnail',
            'croppedSquareThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        playlist_duration = utils.get \
        (
            music_detail_header_renderer,
            'secondSubtitle',
            'runs',
            2,
            'text',
            # Cannot convert to seconds int as it may be, e.g. '6+ hours'
            # func = cleansers.ascii_time,
            # func = cleansers.iso_time,
        )
        playlist_id = utils.get \
        (
            music_playlist_shelf_renderer,
            'playlistId',
        )
        # playlist_track_count = utils.get \
        # (
        #     music_playlist_shelf_renderer,
        #     'collapsedItemCount',
        # )
        playlist_track_count = utils.get \
        (
            music_detail_header_renderer,
            'secondSubtitle',
            'runs',
            0,
            'text',
            func = lambda count: int(count.strip().split(' ')[0]),
        )

        playlist_data = \
        {
            'name':         playlist_title,
            'type':         playlist_type,
            'year':         playlist_year,
            'thumbnail':    playlist_thumbnail,
            'duration':     playlist_duration,
            'id':           playlist_id,
            'total_tracks': playlist_track_count, # This is not 100% correct. Maxes at 100 (??)
            'artist': \
            {
                'name': playlist_artist_name,
                'id':   playlist_artist_id,
            },
            'radio': \
            {
                'playlist_id': playlist_radio_playlist_id,
                'params':      playlist_radio_params,
            },
            'shuffle': \
            {
                'playlist_id': playlist_shuffle_playlist_id,
                'params':      playlist_shuffle_params,
            },
        }

        data = utils.get \
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
            'musicPlaylistShelfRenderer',
        )

        continuation = utils.get \
        (
            data,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )

    assert data

    raw_tracks = utils.get \
    (
        data,
        'contents',
        default = (),
    )

    assert raw_tracks

    tracks = []

    for track in raw_tracks:
        track = utils.first(track)

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
            'overlay',
            'musicItemThumbnailOverlayRenderer',
            'content',
            'musicPlayButtonRenderer',
            'playNavigationEndpoint',
            'watchEndpoint',
        )

        track_music_video_type = utils.get \
        (
            track_watch_endpoint,
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )
        track_id = utils.get \
        (
            track_watch_endpoint,
            'videoId',
        )
        track_title = utils.get \
        (
            track,
            'flexColumns',
            0,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
        )
        track_artist_id = utils.get \
        (
            track,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        track_artist_name = utils.get \
        (
            track,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
        )
        track_album_name = utils.get \
        (
            track,
            'flexColumns',
            2,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
        )
        track_album_id = utils.get \
        (
            track,
            'flexColumns',
            2,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        track_duration = utils.get \
        (
            track,
            'fixedColumns',
            0,
            'musicResponsiveListItemFixedColumnRenderer',
            'text',
            'runs',
            0,
            'text',
            func = cleansers.iso_time,
        )
        track_thumbnail = utils.get \
        (
            track,
            'thumbnail',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_explicit = utils.get \
        (
            track,
            'badges',
            0,
            'musicInlineBadgeRenderer',
            'accessibilityData',
            'accessibilityData',
            'label',
            func = str.lower
        ) == 'explicit'

        track_radio_playlist_id = utils.get \
        (
            track_menu,
            'startRadio',
            'endpoint',
            'watchEndpoint',
            'playlistId',
        )
        track_radio_params = utils.get \
        (
            track_menu,
            'startRadio',
            'endpoint',
            'watchEndpoint',
            'params',
        )

        track_data = \
        {
            'id':        track_id,
            'name':      track_title,
            'duration':  track_duration,
            'thumbnail': track_thumbnail,
            'explicit':  track_explicit,
            'album': \
            {
                'id':   track_album_id,
                'name': track_album_name,
            },
            'artist': \
            {
                'id':   track_artist_id,
                'name': track_artist_name,
            },
            'radio': \
            {
                'playlist_id': track_radio_playlist_id,
                'params': track_radio_params,
            },
        }

        tracks.append(track_data)

    # scraped = \
    # {
    #     'playlist':     playlist_data,
    #     'tracks':       tracks,
    #     'continuation': continuation,
    # }
    scraped = \
    {
        **(playlist_data or {}),
        'tracks':       tracks,
        'continuation': continuation,
    }

    return scraped
