from ..... import utils as ytm_utils
from ..... import constants as ytm_constants
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    if not data:
        return # raise

    if 'continuationContents' in data:
        data = ytm_utils.get_nested \
        (
            data,
            'continuationContents',
            'sectionListContinuation',
        )
    else:
        data = ytm_utils.get_nested \
        (
            data,
            'contents',
            'singleColumnBrowseResultsRenderer',
            'tabs',
            0,
            'tabRenderer',
            'content',
            'sectionListRenderer',
        )

    self._continuation = ytm_utils.get_nested \
    (
        data,
        'continuations',
        0,
        'nextContinuationData',
        'continuation',
    )

    parsed_shelves = []

    shelves = ytm_utils.get_nested(data, 'contents', default = ())[:-1]

    for shelf in shelves:
        shelf = ytm_utils.first_key(shelf)

        shelf_header = ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer')
        shelf_contents = ytm_utils.get_nested(shelf, 'contents', default=[])

        shelf_title = ytm_utils.get_nested(shelf_header, 'title', 'runs', 0, 'text')
        shelf_strapline = ytm_utils.get_nested(shelf_header, 'strapline', 'runs', 0, 'text')

        shelf_items = []

        for item in shelf_contents:
            item = ytm_utils.first_key(item)

            aspect_ratio = ytm_utils.get_nested(item, 'aspectRatio')

            if aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_RECTANGLE_16_9':
                item_thumbnail = ytm_utils.get_nested(item, 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                item_title = ytm_utils.get_nested(item, 'title', 'runs', 0, 'text')
                item_type = 'Video'
                item_artist_name = ytm_utils.get_nested(item, 'subtitle', 'runs', 0, 'text')
                item_artist_id = ytm_utils.get_nested(item, 'subtitle', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId')
                item_views = ytm_utils.get_nested(item, 'subtitle', 'runs', 2, 'text')
                item_id = ytm_utils.get_nested(item, 'navigationEndpoint', 'watchEndpoint', 'videoId')
                item_playlist_id = ytm_utils.get_nested(item, 'navigationEndpoint', 'watchEndpoint', 'playlistId')

                item_data = \
                {
                    'thumbnail': item_thumbnail,
                    'title': item_title,
                    'type': item_type,
                    'artist': \
                    {
                        'name': item_artist_name,
                        'id': item_artist_id,
                    },
                    'views': item_views,
                    'id': item_id,
                    'playlist_id': item_playlist_id,
                }
            elif aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_SQUARE':
                item_subtitle = ytm_utils.get_nested(item, 'subtitle', 'runs', 0, 'text')

                item_thumbnail = ytm_utils.get_nested(item, 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                item_title = ytm_utils.get_nested(item, 'title', 'runs', 0, 'text')
                item_id = ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'browseId')
                item_artist_name = ytm_utils.get_nested(item, 'subtitle', 'runs', 2, 'text')
                item_artist_id = ytm_utils.get_nested(item, 'subtitle', 'runs', 2, 'navigationEndpoint', 'browseEndpoint', 'browseId')
                item_type = ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType', func=lambda page_type: page_type.strip().split('_')[-1].capitalize())

                if item_title == 'Your Mix':
                    continue # Pointless to scrape

                item_data = \
                {
                    'thumbnail': item_thumbnail,
                    'title': item_title,
                    'artist': \
                    {
                        'name': item_artist_name,
                        'id': item_artist_id,
                    },
                    'id': item_id,
                    'type': item_type,
                }
            else:
                return # raise

            shelf_items.append(item_data)

        if not shelf_items:
            continue

        shelf_data = \
        {
            'title': shelf_title,
            'strapline': shelf_strapline,
            'items': shelf_items,
        }

        shelf_obj = containers.HomeShelf(self.api, shelf_data)

        parsed_shelves.append(shelf_obj)

    return parsed_shelves
