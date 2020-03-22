from ..... import utils as ytm_utils
from ..... import constants as ytm_constants
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    # if continuation:
    #     data = self.base.browse(continuation=continuation)
    #
    #     data = ytm_utils.get_nested(data, 'continuationContents', 'sectionListContinuation')
    # else:
    # data = self.base.browse_home()

    if 'continuationContents' in data:
        data = ytm_utils.get_nested(data, 'continuationContents', 'sectionListContinuation')
    else:
        data = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer')


    # from pprint import pprint
    # pprint(data['continuations'])

    self._continuation = ytm_utils.get_nested(data, 'continuations', 0, 'nextContinuationData', 'continuation')
    # 'continuation': ytm_utils.get_nested(data, 'continuations', 0, 'nextContinuationData', 'continuation'),

    scraped = []

    shelves = ytm_utils.get_nested(data, 'contents', default = [])[:-1]

    for shelf in shelves:
        shelf = ytm_utils.first_key(shelf)

        title = ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'title', 'runs', 0, 'text'), # , func=lambda title: title.strip('"'))
        strapline = ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'strapline', 'runs', 0, 'text')

        contents = ytm_utils.get_nested(shelf, 'contents', default=[])

        items = []

        for item in contents:
            aspect_ratio = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'aspectRatio')

            if aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_RECTANGLE_16_9':
                item_data = \
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
                }
            elif aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_SQUARE':
                page_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')

                type_map =  \
                {
                    ytm_constants.PAGE_TYPE_ALBUM: 'Album',
                    ytm_constants.PAGE_TYPE_ARTIST: 'Artist',
                    ytm_constants.PAGE_TYPE_PLAYLIST: 'Playlist',
                    None: None,
                }

                item_data = \
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
                    'type':type_map[page_type],
                }
            else:
                ... # raise

            items.append(item_data)

        # Shelves can have items of different types
        shelf_data = \
        {
            'title': title,
            'strapline': strapline,
            'items': items,
        }

        shelf_obj = containers.HomeShelf(self.api, shelf_data)

        # scraped[title] = shelf_data
        scraped.append(shelf_obj)

    return scraped

    # scraped = \
    # {
    #     'shelves': \
    #     [
    #         {
    #             'title': ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'title', 'runs', 0, 'text'),
    #             'strapline': ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'strapline', 'runs', 0, 'text'),
    #             'items': \
    #             [
    #                 {
    #                     'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_RECTANGLE_16_9': \
    #                     {
    #                         'thumbnail': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
    #                         'title': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text'),
    #                         'type': 'Video',
    #                         'channel': \
    #                         {
    #                             'name': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text'),
    #                             'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
    #                         },
    #                         'views': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'text'),
    #                         'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId'),
    #                         'playlist_id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
    #                     },
    #                     'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_SQUARE': \
    #                     {
    #                         'thumbnail': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
    #                         'title': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text'),
    #                         'subtitle': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text'),
    #                         'channel': \
    #                         {
    #                             'name': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'text'),
    #                             'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
    #                         },
    #                         'id': ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
    #                         'type': \
    #                         {
    #                             ytm_constants.PAGE_TYPE_ALBUM: 'Album',
    #                             ytm_constants.PAGE_TYPE_ARTIST: 'Artist',
    #                             ytm_constants.PAGE_TYPE_PLAYLIST: 'Playlist',
    #                             None: None,
    #                         }[ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')],
    #                     },
    #                 }[ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'aspectRatio')]
    #                 for item in ytm_utils.get_nested(shelf, 'contents', default=[])
    #             ],
    #         }
    #         for shelf in ytm_utils.get_nested(data, 'contents', default = [])[:-1]
    #         for shelf in (ytm_utils.first_key(shelf),)
    #     ],
    # }
    #
    # return scraped
