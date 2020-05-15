'''
Module containing the parser: artist
'''

from .. import utils
from .. import types
from . import decorators
from . import constants
from . import cleansers

@decorators.enforce_parameters
@decorators.catch
def artist(data: dict) -> dict:
    '''
    Parse data: Artist.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_artist('UCTK1maAvqrDlD2agZDGZzjw')
        >>>
        >>> parsed_data = ytm.parsers.artist(data)
        >>>
        >>> parsed_data['name']
        'Take That'
        >>>
    '''

    assert data, 'No data to parse'

    # return data ########

    # Entry Points
    section_list_contents = utils.get \
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
        default = (),
    )
    header = utils.get \
    (
        data,
        'header',
        'musicImmersiveHeaderRenderer',
    )

    assert section_list_contents, 'No section list contents'
    assert header,       'No Header'

    shelves = {}

    # Make this a util?
    for section_list in section_list_contents:
        content_key = list(section_list)[0]
        content     = section_list[content_key]

        if content_key in shelves:
            shelves[content_key].append(content)
        else:
            shelves[content_key] = [content]

    # Artist Shelves
    songs_shelf       = utils.get(shelves, 'musicShelfRenderer', 0)
    description_shelf = utils.get(shelves, 'musicDescriptionShelfRenderer', 0)
    carousel_shelves   = utils.get(shelves, 'musicCarouselShelfRenderer', default = ())

    # Songs Shelf > Items
    songs_shelf_bottom = utils.get \
    (
        songs_shelf,
        'bottomEndpoint',
    )
    songs_shelf_contents = utils.get \
    (
        songs_shelf,
        'contents',
        default = (),
    )

    # Header > Items
    subscribe_button_renderer = utils.get \
    (
        header,
        'subscriptionButton',
        'subscribeButtonRenderer',
    )

    # Songs Shelf > Data
    artist_playlist_id     = utils.get(songs_shelf_bottom, *constants.BROWSE_ENDPOINT_ID)
    artist_playlist_params = utils.get(songs_shelf_bottom, *constants.BROWSE_ENDPOINT_PARAMS)

    # Description Shelf > Data
    artist_views       = utils.get(description_shelf, 'subheader', *constants.RUN_TEXT, func = cleansers.views)
    artist_description = utils.get(description_shelf, 'description', *constants.RUN_TEXT)

    # Header > Data
    artist_name = utils.get \
    (
        header,
        'title',
        *constants.RUN_TEXT,
    )
    artist_id = utils.get \
    (
        subscribe_button_renderer,
        'channelId',
    )
    artist_subscribers = utils.get \
    (
        subscribe_button_renderer,
        'subscriberCountText',
        *constants.RUN_TEXT,
    )

    artist_shelves = {}
    artist_songs   = []

    shelf_identifiers = \
    (
        'albums',
        'singles',
        'videos',
        'songs',
        'playlists',
        'similar_artists',
    )

    shelf_identifier_map = \
    {
        'featured_on':          'playlists',
        'fans_might_also_like': 'similar_artists',
    }

    for shelf_identifier in shelf_identifiers:
        artist_shelves.setdefault(shelf_identifier, None)

    # Songs Shelf > Songs
    for song in songs_shelf_contents:
        song = utils.first(song)

        song_overlay_watch_endpoint = utils.get \
        (
            song,
            'overlay',
            'musicItemThumbnailOverlayRenderer',
            'content',
            'musicPlayButtonRenderer',
            'playNavigationEndpoint',
            'watchEndpoint',
        )
        song_menu_watch_endpoint = utils.get \
        (
            song,
            'menu',
            'menuRenderer',
            'items',
            0,
            'menuNavigationItemRenderer',
            'navigationEndpoint',
            'watchEndpoint',
        )
        song_flex_column_0_run = utils.get \
        (
            song,
            'flexColumns',
            0,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
        )
        song_flex_column_1_run = utils.get \
        (
            song,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
        )
        song_flex_column_2_run = utils.get \
        (
            song,
            'flexColumns',
            2,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
        )

        song_playlist_params = utils.get \
        (
            song_overlay_watch_endpoint,
            'params',
        )
        song_playlist_id = utils.get \
        (
            song_overlay_watch_endpoint,
            'playlistId',
        )
        song_video_id = utils.get \
        (
            song_overlay_watch_endpoint,
            'videoId',
        )
        song_music_video_type = utils.get \
        (
            song_overlay_watch_endpoint,
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )
        song_thumbnail = utils.get \
        (
            song,
            'thumbnail',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        song_title = utils.get \
        (
            song_flex_column_0_run,
            'text',
        )
        song_artist_title = utils.get \
        (
            song_flex_column_1_run,
            'text',
        )
        song_artist_browse_id = utils.get \
        (
            song_flex_column_1_run,
            'navigationEndpoint',
            *constants.BROWSE_ENDPOINT_ID,
        )
        song_album_title = utils.get \
        (
            song_flex_column_2_run,
            'text',
        )
        song_album_browse_id = utils.get \
        (
            song_flex_column_2_run,
            'navigationEndpoint',
            *constants.BROWSE_ENDPOINT_ID,
        )
        song_radio_params = utils.get \
        (
            song_menu_watch_endpoint,
            'params',
        )
        song_radio_playlist_id = utils.get \
        (
            song_menu_watch_endpoint,
            'playlistId',
        )

        song_data = \
        {
            'id':        song_video_id,
            'name':      song_title,
            'thumbnail': song_thumbnail,
            'artist': \
            {
                'name': song_artist_title,
                'id':   song_artist_browse_id,
            },
            'album': \
            {
                'name': song_album_title,
                'id':   song_album_browse_id,
            },
            'radio': \
            {
                'params':      song_radio_params,
                'playlist_id': song_radio_playlist_id,
            },
        }

        artist_songs.append(song_data)

    for shelf in carousel_shelves:
        shelf_header = utils.get \
        (
            shelf,
            'header',
            'musicCarouselShelfBasicHeaderRenderer',
        )
        shelf_browse_endpoint = utils.get \
        (
            shelf_header,
            'endIcons',
            0,
            'iconLinkRenderer',
            'navigationEndpoint',
            'browseEndpoint',
        )
        shelf_contents = utils.get \
        (
            shelf,
            'contents',
            default = (),
        )

        shelf_title = utils.get \
        (
            shelf_header,
            'title',
            'runs',
            0,
            'text',
        )
        shelf_browse_id = utils.get \
        (
            shelf_browse_endpoint,
            'browseId',
        )
        shelf_params = utils.get \
        (
            shelf_browse_endpoint,
            'params',
        )

        shelf_identifier = str(shelf_title).strip().lower().replace(' ', '_')

        shelf_items = []

        if shelf_identifier in shelf_identifier_map:
            shelf_identifier = shelf_identifier_map[shelf_identifier]

        if shelf_identifier not in shelf_identifiers:
            raise Exception \
            (
                f'Unrecognised sheld identifier: {repr(shelf_identifier)}'
            )

        for shelf_item in shelf_contents:
            shelf_item = utils.first(shelf_item)

            if shelf_identifier == 'albums':
                shelf_item_browse_endpoint = utils.get \
                (
                    shelf_item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_menu_item_0_playlist_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )
                shelf_item_menu_item_1_playlist_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )
                shelf_item_subtitle_runs = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                )

                shelf_item_icon_type = utils.get \
                (
                    shelf_item,
                    'subtitleBadges',
                    0,
                    'musicInlineBadgeRenderer',
                    'icon',
                    'iconType',
                )
                shelf_item_thumbnail = utils.get \
                (
                    shelf_item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_title = utils.get \
                (
                    shelf_item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_browse_id = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseId',
                )
                shelf_item_params = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'params',
                )
                shelf_item_page_type = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                shelf_item_type = utils.get \
                (
                    shelf_item_subtitle_runs,
                    0,
                    'text',
                )
                shelf_item_year = utils.get \
                (
                    shelf_item_subtitle_runs,
                    2,
                    'text',
                    func = int,
                )
                shelf_item_shuffle_params = utils.get \
                (
                    shelf_item_menu_item_0_playlist_endpoint,
                    'params',
                )
                shelf_item_shuffle_playlist_id = utils.get \
                (
                    shelf_item_menu_item_0_playlist_endpoint,
                    'playlistId',
                )
                shelf_item_radio_params = utils.get \
                (
                    shelf_item_menu_item_1_playlist_endpoint,
                    'params',
                )
                shelf_item_radio_playlist_id = utils.get \
                (
                    shelf_item_menu_item_1_playlist_endpoint,
                    'playlistId',
                )
                shelf_item_explicit = shelf_item_icon_type == 'MUSIC_EXPLICIT_BADGE'

                shelf_item_data = \
                {
                    'name':      shelf_item_title,
                    'id':        shelf_item_browse_id,
                    'type':      shelf_item_type,
                    'year':      shelf_item_year,
                    'explicit':  shelf_item_explicit,
                    'thumbnail': shelf_item_thumbnail,
                    'shuffle': \
                    {
                        'params':      shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params':      shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'singles':
                shelf_item_browse_endpoint = utils.get \
                (
                    shelf_item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_watch_playlist_endpoint_0 = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )
                shelf_item_watch_playlist_endpoint_1 = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )

                shelf_item_icon_type = utils.get \
                (
                    shelf_item,
                    'subtitleBadges',
                    0,
                    'musicInlineBadgeRenderer',
                    'icon',
                    'iconType',
                )
                shelf_item_thumbnail = utils.get \
                (
                    shelf_item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_name = utils.get \
                (
                    shelf_item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_year = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                    func = int,
                )
                shelf_item_browse_id = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseId',
                )
                shelf_item_playlist_params = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'params',
                )
                shelf_item_page_type = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                shelf_item_playlist_id = utils.get \
                (
                    shelf_item,
                    'thumbnailOverlay',
                    'musicItemThumbnailOverlayRenderer',
                    'content',
                    'musicPlayButtonRenderer',
                    'playNavigationEndpoint',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                shelf_item_shuffle_params = utils.get \
                (
                    shelf_item_watch_playlist_endpoint_0,
                    'params',
                )
                shelf_item_shuffle_playlist_id = utils.get \
                (
                    shelf_item_watch_playlist_endpoint_0,
                    'playlistId',
                )
                shelf_item_radio_params = utils.get \
                (
                    shelf_item_watch_playlist_endpoint_1,
                    'params',
                )
                shelf_item_radio_playlist_id = utils.get \
                (
                    shelf_item_watch_playlist_endpoint_1,
                    'playlistId',
                )
                shelf_item_explicit = shelf_item_icon_type == 'MUSIC_EXPLICIT_BADGE'

                shelf_item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'name':      shelf_item_name,
                    'album': \
                    {
                        'id': shelf_item_browse_id,
                        'playlist_id': shelf_item_playlist_id,
                    },
                    'year':      shelf_item_year,
                    'explicit':  shelf_item_explicit,
                    'shuffle': \
                    {
                        'params':      shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params':      shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'videos':
                shelf_item_watch_endpoint = utils.get \
                (
                    shelf_item,
                    'navigationEndpoint',
                    'watchEndpoint',
                )
                shelf_item_menu_0_watch_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchEndpoint',
                )
                shelf_item_subtitle_run_0 = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                    0,
                )

                shelf_item_music_video_type = utils.get \
                (
                    shelf_item_watch_endpoint,
                    'watchEndpointMusicSupportedConfigs',
                    'watchEndpointMusicConfig',
                    'musicVideoType',
                )
                shelf_item_video_id = utils.get \
                (
                    shelf_item_watch_endpoint,
                    'videoId',
                )
                shelf_item_playlist_id = utils.get \
                (
                    shelf_item_watch_endpoint,
                    'playlistId',
                )
                shelf_item_thumbnail = utils.get \
                (
                    shelf_item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_name = utils.get \
                (
                    shelf_item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_radio_params = utils.get \
                (
                    shelf_item_menu_0_watch_endpoint,
                    'params',
                )
                shelf_item_radio_playlist_id = utils.get \
                (
                    shelf_item_menu_0_watch_endpoint,
                    'playlistId',
                )
                shelf_item_artist_id = utils.get \
                (
                    shelf_item_subtitle_run_0,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                shelf_item_artist_name = utils.get \
                (
                    shelf_item_subtitle_run_0,
                    'text',
                )
                shelf_item_views = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                    -1,
                    'text',
                    func = lambda views: views.strip().split(' ')[0],
                )

                shelf_item_data = \
                {
                    'name':      shelf_item_name,
                    'id':        shelf_item_video_id,
                    'views':     shelf_item_views,
                    'thumbnail': shelf_item_thumbnail,
                    'artist': \
                    {
                        'id':   shelf_item_artist_id,
                        'name': shelf_item_artist_name,
                    },
                    'radio': \
                    {
                        'params':      shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'playlists':
                shelf_item_browse_endpoint = utils.get \
                (
                    shelf_item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_menu_item_0_playlist_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )
                shelf_item_menu_item_1_playlist_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )

                shelf_item_thumbnail = utils.get \
                (
                    shelf_item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_playlist_id = utils.get \
                (
                    shelf_item,
                    'thumbnailOverlay',
                    'musicItemThumbnailOverlayRenderer',
                    'content',
                    'musicPlayButtonRenderer',
                    'playNavigationEndpoint',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                shelf_item_name = utils.get \
                (
                    shelf_item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_playlist_browse_id = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseId',
                )
                shelf_item_page_type = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                shelf_item_type = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_artist = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                    2,
                    'text',
                )
                shelf_item_shuffle_params = utils.get \
                (
                    shelf_item_menu_item_0_playlist_endpoint,
                    'params',
                )
                shelf_item_shuffle_playlist_id = utils.get \
                (
                    shelf_item_menu_item_0_playlist_endpoint,
                    'playlistId',
                )
                shelf_item_radio_params = utils.get \
                (
                    shelf_item_menu_item_1_playlist_endpoint,
                    'params',
                )
                shelf_item_radio_playlist_id = utils.get \
                (
                    shelf_item_menu_item_1_playlist_endpoint,
                    'playlistId',
                )

                shelf_item_data = \
                {
                    'name':      shelf_item_name,
                    'id':        shelf_item_playlist_id,
                    'thumbnail': shelf_item_thumbnail,
                    'shuffle': \
                    {
                        'params':      shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params':      shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'similar_artists':
                shelf_item_browse_endpoint = utils.get \
                (
                    shelf_item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_menu_item_0_playlist_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )
                shelf_item_menu_item_1_playlist_endpoint = utils.get \
                (
                    shelf_item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                )

                shelf_item_page_type = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                shelf_item_browse_id = utils.get \
                (
                    shelf_item_browse_endpoint,
                    'browseId',
                )
                shelf_item_thumbnail = utils.get \
                (
                    shelf_item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_title = utils.get \
                (
                    shelf_item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_subscribers = utils.get \
                (
                    shelf_item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                    func = lambda subscribers: subscribers.split(' ')[0],
                )
                shelf_item_shuffle_params = utils.get \
                (
                    shelf_item_menu_item_0_playlist_endpoint,
                    'params',
                )
                shelf_item_shuffle_playlist_id = utils.get \
                (
                    shelf_item_menu_item_0_playlist_endpoint,
                    'playlistId',
                )
                shelf_item_radio_params = utils.get \
                (
                    shelf_item_menu_item_1_playlist_endpoint,
                    'params',
                )
                shelf_item_radio_playlist_id = utils.get \
                (
                    shelf_item_menu_item_1_playlist_endpoint,
                    'playlistId',
                )

                shelf_item_data = \
                {
                    'name':        shelf_item_title,
                    'id':          shelf_item_browse_id,
                    'subscribers': shelf_item_subscribers,
                    'thumbnail':   shelf_item_thumbnail,
                    'shuffle': \
                    {
                        'params':      shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params':      shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                }

            shelf_items.append(shelf_item_data)

        shelf_data = \
        {
            'title':  shelf_title,
            'items':  shelf_items,
        }

        if shelf_identifier in ('albums', 'singles'):
            shelf_data['params'] = shelf_params

            # Update to correct artist id
            if shelf_browse_id:
                artist_id = str(types.ArtistId(shelf_browse_id))
        elif shelf_identifier == 'videos':
            if shelf_browse_id:
                shelf_browse_id = str(types.ChartPlaylistId(shelf_browse_id)) ### For now. This type will be changed soon.

            shelf_data['playlist_id'] = shelf_browse_id

        artist_shelves[shelf_identifier] = shelf_data

    if artist_playlist_id:
        artist_playlist_id = str(types.ArtistSongsPlaylistId(artist_playlist_id))

    if artist_songs:
        artist_shelves['songs'] = \
        {
            'title':       'Songs',
            'playlist_id': artist_playlist_id,
            'items':       artist_songs,
        }

    # return data ########
    scraped = \
    {
        'name':        artist_name,
        'id':          artist_id,
        'subscribers': artist_subscribers,
        'views':       artist_views,
        'description': artist_description,
        **artist_shelves,
    }

    return scraped
