from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def home(data: dict):
    assert data, 'No data to parse'

    if 'continuationContents' in data:
        data = utils.get \
        (
            data,
            'continuationContents',
            'sectionListContinuation',
        )
    else:
        data = utils.get \
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

    assert data

    # Insert back into data
    continuation = utils.get \
    (
        data,
        'continuations',
        0,
        'nextContinuationData',
        'continuation',
    )

    parsed_shelves = []

    shelves = utils.get \
    (
        data,
        'contents',
        default = (),
    ) # [:-1]

    assert shelves

    for shelf in shelves:
        shelf = utils.first(shelf)

        shelf_header = utils.get \
        (
            shelf,
            'header',
            'musicCarouselShelfBasicHeaderRenderer',
        )
        shelf_contents = utils.get \
        (
            shelf,
            'contents',
            default = (),
        )

        shelf_title = utils.get \
        (
            shelf_header,
            'title',
            'runs',
            0,
            'text',
        )
        shelf_strapline = utils.get \
        (
            shelf_header,
            'strapline',
            'runs',
            0,
            'text',
        )

        shelf_items = []

        for item in shelf_contents:
            item = utils.first(item)

            aspect_ratio = utils.get \
            (
                item,
                'aspectRatio',
            )

            item_thumbnail = utils.get \
            (
                item,
                'thumbnailRenderer',
                'musicThumbnailRenderer',
                'thumbnail',
                'thumbnails',
                -1,
            )
            item_title = utils.get \
            (
                item,
                'title',
                'runs',
                0,
                'text',
            )

            # Find a better way of distinguishing item types?
            if aspect_ratio == 'MUSIC_TWO_ROW_ITEM_THUMBNAIL_ASPECT_RATIO_RECTANGLE_16_9':
                item_artist_name = utils.get \
                (
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                )
                item_artist_id = utils.get \
                (
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_views = utils.get \
                (
                    item,
                    'subtitle',
                    'runs',
                    2,
                    'text',
                )
                item_playlist_id = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'watchEndpoint',
                    'playlistId',
                )
                item_id = utils.get \
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
                item_subtitle = utils.get \
                (
                    item,
                    'subtitle',
                    'runs',
                    0,
                    'text',
                )
                item_artist_name = utils.get \
                (
                    item,
                    'subtitle',
                    'runs',
                    2,
                    'text',
                )
                item_artist_id = utils.get \
                (
                    item,
                    'subtitle',
                    'runs',
                    2,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_id = utils.get \
                (
                    item,
                    'navigationEndpoint',
                    'browseEndpoint',
                    'browseId',
                )
                item_type = utils.get \
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
