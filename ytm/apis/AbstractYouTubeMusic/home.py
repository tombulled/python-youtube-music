from ... import utils as ytm_utils
from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def home(self):
    data = self.base.browse_home()

    scraped = \
    {
        'continuation': ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'continuations', 0, 'nextContinuationData', 'continuation'),
        'shelves': \
        [
            {
                'title': ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'title', 'runs', 0, 'text'),
                'strapline': ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'strapline', 'runs', 0, 'text'),
                'items': \
                [
                    {
                        'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_RECTANGLE_16_9': \
                        {
                            'thumbnail': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                            'title': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text'),
                            'type': 'Video',
                            'channel': \
                            {
                                'name': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text'),
                                'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                            },
                            'views': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'text'),
                            'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId'),
                            'playlist_id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                        },
                        'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_SQUARE': \
                        {
                            'thumbnail': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
                            'title': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text'),
                            'subtitle': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text'),
                            'channel': \
                            {
                                'name': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'text'),
                                'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                            },
                            'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                            'type': \
                            {
                                ytm_constants.PAGE_TYPE_ALBUM: 'Album',
                                ytm_constants.PAGE_TYPE_ARTIST: 'Artist',
                                ytm_constants.PAGE_TYPE_PLAYLIST: 'Playlist',
                                None: None,
                            }[ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')],
                        },
                    }[ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'aspectRatio')]
                    for item in ytm_utils.get_nested(shelf, 'contents', default=[])
                ],
            }
            for shelf in ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', default = [])[:-1]
            for shelf in (ytm_utils.first_key(shelf),)
        ],
    }

    return scraped
