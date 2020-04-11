from .... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def search(data):
    data = ytm_utils.get_nested \
    (
        data,
        'contents',
        'sectionListRenderer',
    )

    query = ytm_utils.get_nested \
    (
        data,
        'contents',
        -1,
        'musicShelfRenderer',
        'bottomEndpoint',
        'searchEndpoint',
        'query',
    )

    results = {}
    top_result = None

    fields = \
    (
        'albums',
        'playlists',
        'videos',
        'artists',
        'songs',
    )

    for field in fields:
        results.setdefault(field, None)

    shelves = ytm_utils.get_nested \
    (
        data,
        'contents',
        default = (),
    )

    for shelf in shelves:
        shelf = ytm_utils.get_nested(shelf, 'musicShelfRenderer')

        shelf_continuation = ytm_utils.get_nested \
        (
            shelf,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )
        shelf_params = ytm_utils.get_nested \
        (
            shelf,
            'bottomEndpoint',
            'searchEndpoint',
            'params',
        )
        shelf_title = ytm_utils.get_nested \
        (
            shelf,
            'title',
            'runs',
            0,
            'text',
        )
        shelf_item_type = ytm_utils.get_nested \
        (
            shelf,
            'contents',
            0,
            'musicResponsiveListItemRenderer',
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
            func = str.lower,
        )

        shelf_items = ytm_utils.get_nested \
        (
            shelf,
            'contents',
            default = (),
        )

        if shelf_title:
            shelf_key = shelf_title.lower().replace(' ', '_')
        elif shelf_item_type:
            shelf_key = f'{shelf_item_type}s'
        else:
            return # raise

        if not shelf_items:
            continue

        results[shelf_key] = []

        for item in shelf_items:
            item = ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer')

            if shelf_key == 'top_result':
                top_result = shelf_item_type

                results.pop(shelf_key)

                continue

            if shelf_key == 'artists':
                item_tracking_params = ytm_utils.get_nested \
                (
                    item,
                    'trackingParams',
                )
                item_type = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    1,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_page_type = ytm_utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                item_playlist_id = ytm_utils.get_nested \
                (
                    item,
                    'doubleTapCommand',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_params = ytm_utils.get_nested \
                (
                    item,
                    'doubleTapCommand',
                    'watchPlaylistEndpoint',
                    'params',
                )
                item_name = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    0,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_subscribers = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                    func = lambda subscribers: subscribers.strip().split(' ')[0],
                )
                item_id = ytm_utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_thumbnail = ytm_utils.get_nested \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                item_radio_playlist_id = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_radio_params = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'params',
                )
                item_shuffle_playlist_id = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_shuffle_params = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'params',
                )

                item_data = \
                {
                    'name': item_name,
                    'id': item_id,
                    'subscribers': item_subscribers,
                    'thumbnail': item_thumbnail,
                    'radio': \
                    {
                        'playlist_id': item_radio_playlist_id,
                        'params': item_radio_params,
                    },
                    'shuffle': \
                    {
                        'playlist_id': item_shuffle_playlist_id,
                        'params': item_shuffle_params,
                    },
                }
            elif shelf_key == 'songs':
                item_tracking_params = ytm_utils.get_nested \
                (
                    item,
                    'trackingParams',
                )
                item_type = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    1,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_share_entity = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'shareEntityEndpoint',
                    'serializedShareEntity',
                )
                item_id = ytm_utils.get_nested \
                (
                    item,
                    'overlay',
                    'musicItemThumbnailOverlayRenderer',
                    'content',
                    'musicPlayButtonRenderer',
                    'playNavigationEndpoint',
                    'watchEndpoint',
                    'videoId',
                )
                item_title = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    0,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_explicit = ytm_utils.get_nested \
                (
                    item,
                    'badges',
                    0,
                    'musicInlineBadgeRenderer',
                    'accessibilityData',
                    'accessibilityData',
                    'label',
                ) == 'Explicit'
                item_duration = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    4,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_thumbnail = ytm_utils.get_nested \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                item_album_name = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    3,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_album_id = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    3,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_radio_playlist_id = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    5,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchEndpoint',
                    'playlistId',
                )
                item_radio_params = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    5,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchEndpoint',
                    'params',
                )

                raw_item_artists = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    default = (),
                )[::2]

                item_artists = []

                for item_artist in raw_item_artists:
                    item_artist_name = ytm_utils.get_nested \
                    (
                        item_artist,
                        'text',
                    )
                    item_artist_id = ytm_utils.get_nested \
                    (
                        item_artist,
                        'navigationEndpoint',
                        'browseEndpoint',
                        'browseId',
                    )

                    item_artist_data = \
                    {
                        'name': item_artist_name,
                        'id':   item_artist_id,
                    }

                    item_artists.append(item_artist_data)

                item_data = \
                {
                    'id':        item_id,
                    'name':      item_title,
                    'explicit':  item_explicit,
                    'duration':  item_duration,
                    'thumbnail': item_thumbnail,
                    'artists':   item_artists,
                    'album': \
                    {
                        'name': item_album_name,
                        'id':   item_album_id,
                    },
                    'radio': \
                    {
                        'playlist_id': item_radio_playlist_id,
                        'params':      item_radio_params,
                    },
                }
            elif shelf_key == 'albums':
                item_tracking_params = ytm_utils.get_nested \
                (
                    item,
                    'trackingParams',
                )
                item_page_type = ytm_utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                item_share_entity = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    -1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'shareEntityEndpoint',
                    'serializedShareEntity',
                )
                item_name = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    0,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_type = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    1,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_artist = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_year = ytm_utils.get_nested \
                (
                    item,
                    'flexColumns',
                    3,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_explicit = ytm_utils.get_nested \
                (
                    item,
                    'badges',
                    0,
                    'musicInlineBadgeRenderer',
                    'accessibilityData',
                    'accessibilityData',
                    'label',
                ) == 'Explicit' # is not None
                item_shuffle_playlist_id = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_shuffle_params = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    0,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'params',
                )
                item_radio_playlist_id = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_radio_params = ytm_utils.get_nested \
                (
                    item,
                    'menu',
                    'menuRenderer',
                    'items',
                    1,
                    'menuNavigationItemRenderer',
                    'navigationEndpoint',
                    'watchPlaylistEndpoint',
                    'params',
                )
                item_id = ytm_utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_thumbnail = ytm_utils.get_nested \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )

                item_data = \
                {
                    'id':        item_id,
                    'name':      item_name,
                    'type':      item_type,
                    'artist':    item_artist,
                    'year':      item_year,
                    'explicit':  item_explicit,
                    'thumbnail': item_thumbnail,
                    'shuffle': \
                    {
                        'playlist_id': item_shuffle_playlist_id,
                        'params':      item_shuffle_params,
                    },
                    'radio': \
                    {
                        'playlist_id': item_radio_playlist_id,
                        'params':      item_radio_params,
                    },
                }
            elif shelf_key == 'videos':
                item_data = \
                {
                    '**tracking_params': ytm_utils.get_nested(item, 'trackingParams'),
                    '**playlist_id': ytm_utils.get_nested(item, 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'playlistId'),
                    '**params': ytm_utils.get_nested(item, 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'params'),
                    '**type': ytm_utils.get_nested(item, 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    '**serialised_share_entity': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),

                    'id': ytm_utils.get_nested(item, 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId'),
                    'title': ytm_utils.get_nested(item, 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'artists': \
                    [
                        ytm_utils.get_nested(run, 'text')
                        for run in ytm_utils.get_nested(item, 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', default=[])
                    ],
                    'views': ytm_utils.get_nested(item, 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                    'duration': ytm_utils.get_nested(item, 'flexColumns', 4, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'radio': \
                    {
                        'playlist_id': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                        'params': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
                    },
                    'thumbnail': ytm_utils.get_nested(item, 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }
            elif shelf_key == 'playlists':
                item_data = \
                {
                    # 'tracking_params': ytm_utils.get_nested(item, 'trackingParams'),
                    # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                    # 'playlist_id': ytm_utils.get_nested(item, 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    # 'params': ytm_utils.get_nested(item, 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    'title': ytm_utils.get_nested(item, 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'type': ytm_utils.get_nested(item, 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # Artist is always 'YouTube Music'
                    # 'artist': ytm_utils.get_nested(item, 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'total_tracks': ytm_utils.get_nested(item, 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                    # 'shuffle': \
                    # {
                    #     'playlist_id': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    #     'params': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    # },
                    # 'radio': \
                    # {
                    #     'playlist_id': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    #     'params': ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    # },
                    # 'browse_id': ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                    # 'page_type': ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                    'id':  ytm_utils.get_nested(item, 'doubleTapCommand', 'watchPlaylistEndpoint', 'playlistId'),
                    # 'params':  ytm_utils.get_nested(item, 'doubleTapCommand', 'watchPlaylistEndpoint', 'params'),
                    'thumbnail': ytm_utils.get_nested(item, 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }
            else:
                return # raise

            results[shelf_key].append(item_data)

    scraped = \
    {
        'query':      query,
        'results':    results,
        'top_result': top_result,
    }

    return scraped
