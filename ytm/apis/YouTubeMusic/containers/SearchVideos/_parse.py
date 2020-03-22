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

        item_obj = containers.SearchVideo(self.api, item_data)

        parsed_items.append(item_obj)

    parsed_data = \
    {
        'items': parsed_items,
        'continuation': continuation,
    }

    return parsed_data
