'''
Module containing the parser: artist
'''

from .. import utils
from . import decorators

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

    content = utils.get \
    (
        data,
        'contents',
        'singleColumnBrowseResultsRenderer',
        'tabs',
        0,
        'tabRenderer',
        'content',
    )

    assert content

    contents = utils.get \
    (
        content,
        'sectionListRenderer',
        'contents',
        default = (),
    )

    assert contents

    shelves = {}

    for content in contents:
        content_key = list(content)[0]
        content = content[content_key]

        if content_key in shelves:
            shelves[content_key].append(content)
        else:
            shelves[content_key] = [content]

    # return {'d':data,'s':shelves,} ###


    header_renderer = utils.get \
    (
        data,
        'header',
        'musicImmersiveHeaderRenderer',
    )
    shelf_renderer = utils.get \
    (
        shelves,
        'musicShelfRenderer',
        0,
    )
    browse_endpoint = utils.get \
    (
        shelf_renderer,
        'bottomEndpoint',
        'browseEndpoint',
    )
    description_shelf_renderer = utils.get \
    (
        shelves,
        'musicDescriptionShelfRenderer',
        0,
    )
    subscribe_button_renderer = utils.get \
    (
        header_renderer,
        'subscriptionButton',
        'subscribeButtonRenderer',
    )

    artist_playlist_id = utils.get \
    (
        browse_endpoint,
        'browseId',
    )
    artist_playlist_params = utils.get \
    (
        browse_endpoint,
        'params',
    )
    artist_name = utils.get \
    (
        header_renderer,
        'title',
        'runs',
        0,
        'text',
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
        'runs',
        0,
        'text',
    )
    artist_views = utils.get \
    (
        description_shelf_renderer,
        'subheader',
        'runs',
        0,
        'text',
        func = lambda views:int(views.strip().split(' ')[0].replace(',', '')),
    )
    artist_description = utils.get \
    (
        description_shelf_renderer,
        'description',
        'runs',
        0,
        'text',
    )

    shelf_songs = utils.get \
    (
        shelf_renderer,
        'contents',
        default = (),
    )

    songs = []

    for song in shelf_songs:
        song = utils.get \
        (
            song,
            'musicResponsiveListItemRenderer',
        )

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
            'browseEndpoint',
            'browseId',
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
            'browseEndpoint',
            'browseId',
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
            'name':     song_title,
            'thumbnail': song_thumbnail,
            'artist': \
            {
                'name': song_artist_title,
                'id':    song_artist_browse_id,
            },
            'album': \
            {
                'name': song_album_title,
                'id':    song_album_browse_id,
            },
            'radio': \
            {
                'params':      song_radio_params,
                'playlist_id': song_radio_playlist_id,
            },
        }

        songs.append(song_data)

    shelves = utils.get \
    (
        shelves,
        'musicCarouselShelfRenderer',
        default = (),
    )

    shelves_data = {}

    fields = \
    (
        'albums',
        'singles',
        'videos',
        'songs',
        'playlists',
        'similar_artists',
    )

    for field in fields:
        shelves_data.setdefault(field, None)

    # artist_params = \
    # {
    #     'abums': None,
    #     'singles': None,
    # }

    for shelf in shelves:
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

        shelf_identifier = shelf_title.strip().lower().replace(' ', '_') \
            if shelf_title else None

        shelf_items = utils.get \
        (
            shelf,
            'contents',
            default = (),
        )

        items = []

        for item in shelf_items:
            item = utils.get \
            (
                item,
                'musicTwoRowItemRenderer',
            )

            if shelf_identifier == 'albums':
                shelf_item_browse_endpoint = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_menu_item_0_playlist_endpoint = utils.get \
                (
                    item,
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
                    item,
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
                    item,
                    'subtitle',
                    'runs',
                )

                shelf_item_icon_type = utils.get \
                (
                    item,
                    'subtitleBadges',
                    0,
                    'musicInlineBadgeRenderer',
                    'icon',
                    'iconType',
                )
                shelf_item_thumbnail = utils.get \
                (
                    item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_title = utils.get \
                (
                    item,
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

                item_data = \
                {
                    'name':      shelf_item_title,
                    'id':        shelf_item_browse_id,
                    'type':      shelf_item_type,
                    'year':      shelf_item_year,
                    'explicit':  shelf_item_explicit,
                    # 'params':    shelf_item_params,
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
                # return item ###

                shelf_item_browse_endpoint = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_watch_playlist_endpoint_0 = utils.get \
                (
                    item,
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
                    item,
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
                    item,
                    'subtitleBadges',
                    0,
                    'musicInlineBadgeRenderer',
                    'icon',
                    'iconType',
                )
                shelf_item_thumbnail = utils.get \
                (
                    item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_name = utils.get \
                (
                    item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_year = utils.get \
                (
                    item,
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
                    item,
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

                item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'name':      shelf_item_name,
                    'album': \
                    {
                        'id': shelf_item_browse_id,
                        'playlist_id': shelf_item_playlist_id,
                    },
                    # 'album_id':  shelf_item_browse_id,
                    'year':      shelf_item_year,
                    'explicit':  shelf_item_explicit,
                    # 'playlist': \
                    # {
                    #     'params': shelf_item_playlist_params,
                    #     'id':     shelf_item_playlist_id,
                    # },
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
                    item,
                    'navigationEndpoint',
                    'watchEndpoint',
                )
                shelf_item_menu_0_watch_endpoint = utils.get \
                (
                    item,
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
                    item,
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
                    item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_name = utils.get \
                (
                    item,
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
                    item,
                    'subtitle',
                    'runs',
                    -1,
                    'text',
                    func = lambda views: views.strip().split(' ')[0],
                )

                item_data = \
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
            elif shelf_identifier == 'featured_on':
                shelf_item_browse_endpoint = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_menu_item_0_playlist_endpoint = utils.get \
                (
                    item,
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
                    item,
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
                    item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_playlist_id = utils.get \
                (
                    item,
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
                    item,
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
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_artist = utils.get \
                (
                    item,
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

                item_data = \
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
            elif shelf_identifier == 'fans_might_also_like':
                shelf_item_browse_endpoint = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                )
                shelf_item_menu_item_0_playlist_endpoint = utils.get \
                (
                    item,
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
                    item,
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
                    item,
                    'thumbnailRenderer',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                shelf_item_title = utils.get \
                (
                    item,
                    'title',
                    'runs',
                    0,
                    'text',
                )
                shelf_item_subscribers = utils.get \
                (
                    item,
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

                item_data = \
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
            else:
                return # raise

            items.append(item_data)

        if shelf_identifier == 'albums':
            shelf_data = \
            {
                'title':  shelf_title,
                'params': shelf_params,
                'items':  items,
            }
            # shelf_data = items

            # artist_params[shelf_identifier] = shelf_params

            # Update to correct artist id
            if shelf_browse_id:
                artist_id = shelf_browse_id
        elif shelf_identifier == 'singles':
            shelf_data = \
            {
                'title':  shelf_title,
                'params': shelf_params,
                'items':  items,
            }
            # shelf_data = items

            # artist_params[shelf_identifier] = shelf_params

            # Update to correct artist id
            if shelf_browse_id:
                artist_id = shelf_browse_id
        elif shelf_identifier == 'videos':
            if shelf_browse_id and shelf_browse_id.startswith('VL'):
                shelf_browse_id = shelf_browse_id[2:]

            shelf_data = \
            {
                'title':       shelf_title,
                'playlist_id': shelf_browse_id,
                'items':       items,
            }
        elif shelf_identifier == 'featured_on':
            shelf_data = \
            {
                'title': shelf_title,
                'items': items,
            }

            shelf_identifier = 'playlists'
        elif shelf_identifier == 'fans_might_also_like':
            shelf_data = \
            {
                'title': shelf_title,
                'items': items,
            }

            shelf_identifier = 'similar_artists'
        else:
            return # raise

        shelves_data[shelf_identifier] = shelf_data

    if artist_playlist_id and artist_playlist_id.startswith('VL'):
        artist_playlist_id = artist_playlist_id[2:]

    shelves_data['songs'] = \
    {
        'title':       'Songs',
        'playlist_id': artist_playlist_id,
        'items':       songs,
    } if songs else None

    scraped = \
    {
        'name':        artist_name,
        'id':          artist_id,
        'subscribers': artist_subscribers,
        'views':       artist_views,
        'description': artist_description,
    }

    scraped.update(shelves_data)

    return scraped
