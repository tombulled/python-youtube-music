from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search(data: dict):
    assert data, 'No data to parse'

    data = utils.get \
    (
        data,
        'contents',
        'sectionListRenderer',
    )

    assert data

    query = utils.get \
    (
        data,
        'contents',
        -1,
        'musicShelfRenderer',
        'bottomEndpoint',
        'searchEndpoint',
        'query',
    )

    fields = \
    (
        'albums',
        'playlists',
        'videos',
        'artists',
        'songs',
    )

    results = dict.fromkeys(fields)

    shelves = utils.get \
    (
        data,
        'contents',
        default = (),
    )

    assert shelves

    for shelf in shelves:
        shelf = utils.first(shelf)

        shelf_continuation = utils.get \
        (
            shelf,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )
        shelf_params = utils.get \
        (
            shelf,
            'bottomEndpoint',
            'searchEndpoint',
            'params',
        )
        shelf_title = utils.get \
        (
            shelf,
            'title',
            'runs',
            0,
            'text',
        )
        shelf_item_type = utils.get \
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

        shelf_items = utils.get \
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
            item = utils.first(item)

            if shelf_key == 'top_result':
                results[shelf_key] = shelf_item_type

                continue

            if shelf_key == 'artists':
                item_tracking_params = utils.get \
                (
                    item,
                    'trackingParams',
                )
                item_type = utils.get \
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
                item_page_type = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                item_playlist_id = utils.get \
                (
                    item,
                    'doubleTapCommand',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_params = utils.get \
                (
                    item,
                    'doubleTapCommand',
                    'watchPlaylistEndpoint',
                    'params',
                )
                item_name = utils.get \
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
                item_subscribers = utils.get \
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
                item_id = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_thumbnail = utils.get \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                item_radio_playlist_id = utils.get \
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
                item_radio_params = utils.get \
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
                item_shuffle_playlist_id = utils.get \
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
                item_shuffle_params = utils.get \
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
                    'name':        item_name,
                    'id':          item_id,
                    'subscribers': item_subscribers,
                    'thumbnail':   item_thumbnail,
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
                item_tracking_params = utils.get \
                (
                    item,
                    'trackingParams',
                )
                item_share_entity = utils.get \
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
                item_id = utils.get \
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
                item_name = utils.get \
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
                item_explicit = utils.get \
                (
                    item,
                    'badges',
                    0,
                    'musicInlineBadgeRenderer',
                    'accessibilityData',
                    'accessibilityData',
                    'label',
                ) == 'Explicit'
                item_duration = utils.get \
                (
                    item,
                    'flexColumns',
                    -1,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_thumbnail = utils.get \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                item_album_name = utils.get \
                (
                    item,
                    'flexColumns',
                    -2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_album_id = utils.get \
                (
                    item,
                    'flexColumns',
                    -2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_radio_playlist_id = utils.get \
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
                item_radio_params = utils.get \
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

                raw_item_artists = utils.get \
                (
                    item,
                    'flexColumns',
                    -3,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    default = (),
                )[::2]

                item_artists = []

                for item_artist in raw_item_artists:
                    item_artist_name = utils.get \
                    (
                        item_artist,
                        'text',
                    )
                    item_artist_id = utils.get \
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
                    'name':      item_name,
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
                item_tracking_params = utils.get \
                (
                    item,
                    'trackingParams',
                )
                item_page_type = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                item_share_entity = utils.get \
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
                item_name = utils.get \
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
                item_type = utils.get \
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
                item_artist = utils.get \
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
                item_year = utils.get \
                (
                    item,
                    'flexColumns',
                    3,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                    func = int,
                )
                item_explicit = utils.get \
                (
                    item,
                    'badges',
                    0,
                    'musicInlineBadgeRenderer',
                    'accessibilityData',
                    'accessibilityData',
                    'label',
                ) == 'Explicit' # is not None
                item_shuffle_playlist_id = utils.get \
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
                item_shuffle_params = utils.get \
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
                item_radio_playlist_id = utils.get \
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
                item_radio_params = utils.get \
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
                item_id = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_thumbnail = utils.get \
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
                item_tracking_params = utils.get \
                (
                    item,
                    'trackingParams',
                )
                item_share_entity = utils.get \
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
                item_id = utils.get \
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
                item_name = utils.get \
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
                item_views = utils.get \
                (
                    item,
                    'flexColumns',
                    -2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                    func = lambda views: views.strip().split(' ')[0],
                )
                item_duration = utils.get \
                (
                    item,
                    'flexColumns',
                    -1,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_thumbnail = utils.get \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                item_radio_playlist_id = utils.get \
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
                item_radio_params = utils.get \
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

                raw_item_artists = utils.get \
                (
                    item,
                    'flexColumns',
                    -3,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    default = (),
                )

                item_artists = []

                for item_artist in raw_item_artists:
                    item_artist_name = utils.get \
                    (
                        item_artist,
                        'text',
                    )

                    item_artists.append(item_artist_name)

                item_data = \
                {
                    'id':        item_id,
                    'name':      item_name,
                    'views':     item_views,
                    'duration':  item_duration,
                    'thumbnail': item_thumbnail,
                    'artists':   item_artists,
                    'radio': \
                    {
                        'playlist_id': item_radio_playlist_id,
                        'params':      item_radio_params,
                    },
                }
            elif shelf_key == 'playlists':
                item_tracking_params = utils.get \
                (
                    item,
                    'trackingParams',
                )
                item_browse_id = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_page_type = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                )
                item_id = utils.get \
                (
                    item,
                    'doubleTapCommand',
                    'watchPlaylistEndpoint',
                    'playlistId',
                )
                item_name = utils.get \
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
                item_artist = utils.get \
                (
                    item,
                    'flexColumns',
                    -2,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                )
                item_total_tracks = utils.get \
                (
                    item,
                    'flexColumns',
                    -1,
                    'musicResponsiveListItemFlexColumnRenderer',
                    'text',
                    'runs',
                    0,
                    'text',
                    func = lambda total: total.strip().split(' ')[0],
                    # Cant map to int, may be '100+' ^^^
                )
                item_thumbnail = utils.get \
                (
                    item,
                    'thumbnail',
                    'musicThumbnailRenderer',
                    'thumbnail',
                    'thumbnails',
                    -1,
                )
                item_shuffle_playlist_id = utils.get \
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
                item_shuffle_params = utils.get \
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
                item_radio_playlist_id = utils.get \
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
                item_radio_params = utils.get \
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
                    'id':           item_id,
                    'name':         item_name,
                    'artist':       item_artist,
                    'total_tracks': item_total_tracks,
                    'thumbnail':    item_thumbnail,
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
            else:
                return # raise

            results[shelf_key].append(item_data)

    return results
