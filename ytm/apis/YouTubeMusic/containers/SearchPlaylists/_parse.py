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

        item_obj = containers.SearchPlaylist(self.api, item_data)

        parsed_items.append(item_obj)

    parsed_data = \
    {
        'items': parsed_items,
        'continuation': continuation,
    }

    return parsed_data
