from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    items = ytm_utils.get_nested(data, 'continuationContents', 'musicShelfContinuation', 'contents')

    continuation = ytm_utils.get_nested(data, 'continuationContents', 'musicShelfContinuation', 'continuations', 0, 'nextContinuationData', 'continuation')

    parsed_items = []

    for item in items:
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

        item_obj = containers.SearchAlbum(self.api, item_data)

        parsed_items.append(item_obj)

    parsed_data = \
    {
        'items': parsed_items,
        'continuation': continuation,
    }

    return parsed_data
