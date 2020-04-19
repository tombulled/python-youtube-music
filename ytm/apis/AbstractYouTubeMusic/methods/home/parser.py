from ... import utils

__parser__ = __name__.split('.')[-1]
__all__ = (__parser__,)

def parse(data):
    if not data:
        return # raise

    if 'continuationContents' in data:
        data = utils.get_nested \
        (
            data,
            'continuationContents',
            'sectionListContinuation',
        )
    else:
        data = utils.get_nested \
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

    # Insert back into data
    continuation = utils.get_nested \
    (
        data,
        'continuations',
        0,
        'nextContinuationData',
        'continuation',
    )

    parsed_shelves = []

    shelves = utils.get_nested \
    (
        data,
        'contents',
        default = (),
    )[:-1]

    for shelf in shelves:
        shelf = utils.first_key(shelf)

        shelf_header = utils.get_nested \
        (
            shelf,
            'header',
            'musicCarouselShelfBasicHeaderRenderer',
        )
        shelf_contents = utils.get_nested \
        (
            shelf,
            'contents',
            default = (),
        )

        shelf_title = utils.get_nested \
        (
            shelf_header,
            'title',
            'runs',
            0,
            'text',
        )
        shelf_strapline = utils.get_nested \
        (
            shelf_header,
            'strapline',
            'runs',
            0,
            'text',
        )

        shelf_items = []

        for item in shelf_contents:
            item = utils.first_key(item)

            aspect_ratio = utils.get_nested \
            (
                item,
                'aspectRatio',
            )

            item_thumbnail = utils.get_nested \
            (
                item,
                'thumbnailRenderer',
                'musicThumbnailRenderer',
                'thumbnail',
                'thumbnails',
                -1,
            )
            item_title = utils.get_nested \
            (
                item,
                'title',
                'runs',
                0,
                'text',
            )

            # Find a better way of distinguishing item types?
            if aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_RECTANGLE_16_9':
                item_artist_name = utils.get_nested \
                (
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                )
                item_artist_id = utils.get_nested \
                (
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_views = utils.get_nested \
                (
                    item,
                    'subtitle',
                    'runs',
                    2,
                    'text',
                )
                item_playlist_id = utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'watchEndpoint',
                    'playlistId',
                )
                item_id = utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'watchEndpoint',
                    'videoId',
                )
                item_type = 'Video'

                item_data = \
                {
                    'id':          item_id,
                    'name':        item_title,
                    'type':        item_type,
                    'views':       item_views,
                    'playlist_id': item_playlist_id,
                    'thumbnail':   item_thumbnail,
                    'artist': \
                    {
                        'name': item_artist_name,
                        'id':   item_artist_id,
                    },
                }
            elif aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_SQUARE':
                item_subtitle = utils.get_nested \
                (
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                )
                item_artist_name = utils.get_nested \
                (
                    item,
                    'subtitle',
                    'runs',
                    2,
                    'text',
                )
                item_artist_id = utils.get_nested \
                (
                    item,
                    'subtitle',
                    'runs',
                    2,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_id = utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_type = utils.get_nested \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseEndpointContextSupportedConfigs',
                    'browseEndpointContextMusicConfig',
                    'pageType',
                    func = lambda page_type: page_type.strip().split('_')[-1].capitalize(),
                )

                if item_title == 'Your Mix':
                    continue # Pointless to process

                item_data = \
                {
                    'id':        item_id,
                    'name':      item_title,
                    'type':      item_type,
                    'thumbnail': item_thumbnail,
                    'artist': \
                    {
                        'name': item_artist_name,
                        'id':   item_artist_id,
                    },
                }
            else:
                return # raise

            shelf_items.append(item_data)

        if not shelf_items:
            continue

        shelf_data = \
        {
            'title':     shelf_title,
            'strapline': shelf_strapline,
            'items':     shelf_items,
        }

        parsed_shelves.append(shelf_data)

    parsed_data = \
    {
        'continuation': continuation,
        'shelves':      parsed_shelves,
    }

    return parsed_data
