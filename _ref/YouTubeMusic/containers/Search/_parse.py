from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    data = ytm_utils.get_nested(data, 'contents', 'sectionListRenderer')

    query = ytm_utils.get_nested(data, 'contents', -1, 'musicShelfRenderer', 'bottomEndpoint', 'searchEndpoint', 'query')
    # return data


    scraped = \
    {
        'query': query,
        'results': {},
        'top_result': None,
    }

    # print('search:query ->', query)

    for field in ('albums', 'playlists', 'videos', 'artists', 'songs'):
        scraped['results'].setdefault(field, None)

    # print('search:setdefault:', scraped)

    shelves = ytm_utils.get_nested(data, 'contents', default=[])

    # from pprint import pprint
    # pprint(shelves)

    # utils.get_nested(data, 'contents', 'sectionListRenderer', 'contents', 0, 'musicShelfRenderer', 'continuations', 0, 'nextContinuationData', 'continuation'),

    for shelf in shelves:
        # pprint(shelf)

        # print(ytm_utils.get_nested(shelf, 'musicShelfRenderer'))
        continuation = ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'continuations', 0, 'nextContinuationData', 'continuation')
        title = ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'title', 'runs', 0, 'text')
        item_type = ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'contents', 0, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=str.lower)
        if title:
            shelf_key = title.lower().replace(' ', '_')
        elif item_type:
            item_type + 's'
        else:
            return # raise
        # print(repr(title), repr(item_type), '->', shelf_key)
        params = ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'bottomEndpoint', 'searchEndpoint', 'params')

        items = ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'contents', default=[])

        scraped['results'][shelf_key] = \
        {
            'params': params,
            'continuation': continuation,
            'items': [] if items else None,
        }

        for item in items:
            if shelf_key == 'top_result':
                scraped[shelf_key] = item_type

                continue
            elif shelf_key == 'artists':
                item_data = \
                {
                    # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                    'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'subscribers': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'subscribers': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                    'radio': \
                    {
                        'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    },
                    'shuffle': \
                    {
                        'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    },
                    'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                    # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                    # 'playlist_id':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'playlistId'),
                    # 'params':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'params'),
                    'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }
                # shelf_items.append(item_data)

                # item_obj = containers.SearchArtist(self.api, item)
                container = containers.SearchArtist
            elif shelf_key == 'songs':
                item_data = \
                {
                    # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                    # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                    #'watch': \
                    #{
                    'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId'),
                    # 'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'playlistId'),
                    # 'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'params'),
                    #},
                    'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'artists': \
                    [
                        {
                            'title': ytm_utils.get_nested(run, 'text'),
                            # 'click_tracking_params': ytm_utils.get_nested(run, 'navigationEndpoint', 'clickTrackingParams'),
                            'id': ytm_utils.get_nested(run, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                            # 'page_type': ytm_utils.get_nested(run, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                        }
                        for run in ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', default=[])[::2]
                    ],
                    'explicit': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'badges', 0, 'musicInlineBadgeRenderer', 'accessibilityData', 'accessibilityData', 'label') == 'Explicit',
                    'album': \
                    {
                        'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'click_tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'clickTrackingParams'),
                        'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                        # Will say album, even if its only a single
                        # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                    },
                    'duration': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 4, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'seconds': ytm_utils.parse_duration(duration) if duration else None,
                    # },
                    # 'serialised_share_entity': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),
                    # All these are already provided
                    'radio': \
                    {
                        # 'video_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId'),
                        'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                        'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
                    },
                    'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }

                container = containers.SearchSong
            elif shelf_key == 'albums':
                item_data = \
                {
                    # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                    # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                    'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'artist': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'year': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'year': int(year) if year and year.isdigit() else None,
                    'explicit': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'badges', 0, 'musicInlineBadgeRenderer', 'accessibilityData', 'accessibilityData', 'label') == 'Explicit', # is not None,
                    # 'shuffle': \
                    # {
                    #     'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    #     'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    # },
                    'radio': \
                    {
                        'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    },
                    # 'serialised_share_entity': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', -1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),
                    'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                    # page_type: 'MUSIC_PAGE_TYPE_ALBUM'
                    # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                    'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }

                container = containers.SearchAlbum
            elif shelf_key == 'videos':
                item_data = \
                {
                    # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                    # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                    'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId'),
                    # 'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'playlistId'),
                    # 'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'params'),
                    'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    #'artist': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    #'artists': \
                    #[
                    #    ytm_utils.get_nested(flex_column, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
                    #    for flex_column in ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', default=[])[2:-2]
                    #],
                    'artists': \
                    [
                        ytm_utils.get_nested(run, 'text')
                        for run in ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', default=[])
                    ],
                    'views': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                    # },
                    'duration': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 4, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'serialised_share_entity': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),
                    'radio': \
                    {
                        # 'video_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId'),
                        'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                        'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
                    },
                    'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }

                container = containers.SearchVideo
            elif shelf_key == 'playlists':
                item_data = \
                {
                    # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                    # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                    # 'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    # 'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # Artist is always 'YouTube Music'
                    # 'artist': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    'total_tracks': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                    # 'shuffle': \
                    # {
                    #     'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    #     'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    # },
                    # 'radio': \
                    # {
                    #     'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                    #     'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                    # },
                    # 'browse_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                    # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                    'id':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'playlistId'),
                    # 'params':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'params'),
                    'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                }

                container = containers.SearchPlaylist
            else:
                from pprint import pprint
                pprint(data)
                return # raise

            item_obj = container(self.api, item_data)

            # scraped[shelf_key].append(item_data)
            scraped['results'][shelf_key]['items'].append(item_obj)

    return scraped

    """
    'results': \
    {
        ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'title', 'runs', 0, 'text', func=lambda title: title.strip().lower().replace(' ', '_')) \
        or \
        ytm_utils.get_nested([result for chip in ytm_utils.get_nested(raw_data, 'header', 'musicHeaderRenderer', 'header', 'chipCloudRenderer', 'chips') for result in ((ytm_utils.get_nested(chip, 'chipCloudChipRenderer', 'text', 'runs', 0, 'text'),) if ytm_utils.get_nested(chip, 'chipCloudChipRenderer', 'style', 'styleType') == 'STYLE_PRIMARY' else ())], 0, func=lambda title: title.strip().lower().replace(' ', '_'))\
        : \
        {
            # 'click_tracking_params': ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'bottomEndpoint', 'clickTrackingParams'),
            # 'query': ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'bottomEndpoint', 'searchEndpoint', 'query'),
            'params': ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'bottomEndpoint', 'searchEndpoint', 'params'),
            'items': \
            [
                # This approach is great, however it renders *everything*, so functions used here
                # Need to be able to cope with erronerous data
                {
                    'Songs': \
                    {
                        # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                        # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                        #'watch': \
                        #{
                        'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId'),
                        # 'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'playlistId'),
                        # 'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'params'),
                        #},
                        'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        'artists': \
                        [
                            {
                                'title': ytm_utils.get_nested(run, 'text'),
                                # 'click_tracking_params': ytm_utils.get_nested(run, 'navigationEndpoint', 'clickTrackingParams'),
                                'id': ytm_utils.get_nested(run, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                                # 'page_type': ytm_utils.get_nested(run, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                            }
                            for run in ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', default=[])[::2]
                        ],
                        'explicit': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'badges', 0, 'musicInlineBadgeRenderer', 'accessibilityData', 'accessibilityData', 'label') == 'Explicit',
                        'album': \
                        {
                            'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                            # 'click_tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'clickTrackingParams'),
                            'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                            # Will say album, even if its only a single
                            # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                        },
                        'duration': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 4, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                            # 'seconds': ytm_utils.parse_duration(duration) if duration else None,
                        # },
                        # 'serialised_share_entity': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),
                        # All these are already provided
                        'radio': \
                        {
                            # 'video_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId'),
                            'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                            'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
                        },
                        'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                    },
                    'Artists': \
                    {
                        # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                        'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'subscribers': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        'subscribers': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                        'radio': \
                        {
                            'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                            'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        },
                        'shuffle': \
                        {
                            'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                            'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        },
                        'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                        # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                        # 'playlist_id':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'playlistId'),
                        # 'params':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'params'),
                        'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                    },
                    'Videos': \
                    {
                        # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                        # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                        'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId'),
                        # 'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'playlistId'),
                        # 'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'params'),
                        'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        #'artist': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        #'artists': \
                        #[
                        #    ytm_utils.get_nested(flex_column, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
                        #    for flex_column in ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', default=[])[2:-2]
                        #],
                        'artists': \
                        [
                            ytm_utils.get_nested(run, 'text')
                            for run in ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', default=[])
                        ],
                        'views': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                        # },
                        'duration': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 4, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'serialised_share_entity': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),
                        'radio': \
                        {
                            # 'video_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId'),
                            'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                            'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
                        },
                        'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                    },
                    'Playlists': \
                    {
                        # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                        # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                        # 'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        # 'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # Artist is always 'YouTube Music'
                        # 'artist': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        'total_tracks': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=lambda subscribers: subscribers.strip().split(' ')[0]),
                        # 'shuffle': \
                        # {
                        #     'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        #     'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        # },
                        # 'radio': \
                        # {
                        #     'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        #     'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        # },
                        # 'browse_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                        # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                        'id':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'playlistId'),
                        # 'params':  ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'doubleTapCommand', 'watchPlaylistEndpoint', 'params'),
                        'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                    },
                    'Albums': \
                    {
                        # 'tracking_params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'trackingParams'),
                        # 'vertical_gradient_layer_colours': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'background', 'verticalGradient', 'gradientLayerColors'),
                        'title': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        'artist': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        'year': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 3, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                        # 'year': int(year) if year and year.isdigit() else None,
                        'explicit': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'badges', 0, 'musicInlineBadgeRenderer', 'accessibilityData', 'accessibilityData', 'label'), # is not None,
                        # 'shuffle': \
                        # {
                        #     'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                        #     'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        # },
                        'radio': \
                        {
                            'playlist_id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'),
                            'params': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params'),
                        },
                        # 'serialised_share_entity': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', -1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'shareEntityEndpoint', 'serializedShareEntity'),
                        'id': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                        # page_type: 'MUSIC_PAGE_TYPE_ALBUM'
                        # 'page_type': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType'),
                        'thumbnail': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                    },
                    # 'Top Result': ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                    # Also: 'Top result'. However this result is included in the other shelves
                }.get(ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'title', 'runs', 0, 'text') or ytm_utils.get_nested([result for chip in ytm_utils.get_nested(raw_data, 'header', 'musicHeaderRenderer', 'header', 'chipCloudRenderer', 'chips') for result in ((ytm_utils.get_nested(chip, 'chipCloudChipRenderer', 'text', 'runs', 0, 'text'),) if ytm_utils.get_nested(chip, 'chipCloudChipRenderer', 'style', 'styleType') == 'STYLE_PRIMARY' else ())], 0))
                for item in ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'contents', default=[])
            ],
        } \
        if ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'title', 'runs', 0, 'text') != 'Top result' \
        else ytm_utils.get_nested(shelf, 'musicShelfRenderer', 'contents', 0, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text', func=str.lower)
        # if
        # else
        for shelf in ytm_utils.get_nested(data, 'contents', default=[])
    },
}

for field in ('albums', 'playlists', 'videos', 'artists', 'songs'):
    scraped['results'].setdefault(field, None)
    """

    return scraped
