'''
Module containing the parser: home
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def home(data: dict) -> dict:
    '''
    Parse data: Home.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_home()
        >>>
        >>> parsed_data = ytm.parsers.home(data)
        >>>
        >>> parsed_data['shelves'][0]['name']
        'Morning sunshine'
        >>>
    '''

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

    assert data, 'No section list'

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
    )

    assert shelves, 'No shelves'

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
            func = lambda strapline: strapline.strip() or None
        )

        shelf_items = []

        for item in shelf_contents:
            item = utils.first(item)

            item_menu_items = utils.get \
            (
                item,
                'menu',
                'menuRenderer',
                'items',
                default = (),
            )

            item_menu = {}

            for menu_item in item_menu_items:
                menu_item = utils.first(menu_item)

                for key, val in menu_item.copy().items():
                    if not key.startswith('default'):
                        continue

                    new_key = key.replace('default', '')
                    new_key = new_key[0].lower() + new_key[1:]

                    menu_item[new_key] = menu_item.pop(key)

                menu_text = utils.get \
                (
                    menu_item,
                    'text',
                    'runs',
                    0,
                    'text',
                )
                menu_icon = utils.get \
                (
                    menu_item,
                    'icon',
                    'iconType',
                )
                menu_endpoint = utils.get \
                (
                    menu_item,
                    'navigationEndpoint',
                )

                if not menu_endpoint:
                    continue

                menu_identifier = menu_text[0].lower() + menu_text.title()[1:].replace(' ', '') \
                    if menu_text else None

                menu_item_data = \
                {
                    'text':     menu_text,
                    'icon':     menu_icon,
                    'endpoint': menu_endpoint,
                }

                item_menu[menu_identifier] = menu_item_data

            # return item_menu

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
            # item_shuffle_playlist_id = utils.get \
            # (
            #     item_menu,
            #     'shufflePlay',
            #     'endpoint',
            #     'watchPlaylistEndpoint',
            #     'playlistId',
            # )
            # item_shuffle_params = utils.get \
            # (
            #     item_menu,
            #     'shufflePlay',
            #     'endpoint',
            #     'watchPlaylistEndpoint',
            #     'params',
            # )
            # item_radio_playlist_id = utils.get \
            # (
            #     item_menu,
            #     'startRadio',
            #     'endpoint',
            #     'watchPlaylistEndpoint',
            #     'playlistId',
            # )
            # item_radio_params = utils.get \
            # (
            #     item_menu,
            #     'startRadio',
            #     'endpoint',
            #     'watchPlaylistEndpoint',
            #     'params',
            # )
            item_shuffle_endpoint = utils.get \
            (
                item_menu,
                'shufflePlay',
                'endpoint',
                func = lambda endpoint: utils.first(dict((endpoint.popitem(),))),
            )
            item_radio_endpoint = utils.get \
            (
                item_menu,
                'startRadio',
                'endpoint',
                func = lambda endpoint: utils.first(dict((endpoint.popitem(),))),
            )

            item_shuffle_playlist_id = utils.get \
            (
                item_shuffle_endpoint,
                'playlistId',
            )
            item_shuffle_params = utils.get \
            (
                item_shuffle_endpoint,
                'params',
            )
            item_radio_playlist_id = utils.get \
            (
                item_radio_endpoint,
                'playlistId',
            )
            item_radio_params = utils.get \
            (
                item_radio_endpoint,
                'params',
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
                    func = lambda views: views.strip().split(' ')[0],
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
                    'thumbnail':   item_thumbnail,
                    'artist': \
                    {
                        'name': item_artist_name,
                        'id':   item_artist_id,
                    },
                    'radio': \
                    {
                        'playlist_id': item_radio_playlist_id,
                        'params':      item_radio_params,
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

                if item_type == 'Playlist':
                    item_data = \
                    {
                        'id':        item_id,
                        'name':      item_title,
                        'type':      item_type,
                        'thumbnail': item_thumbnail,
                        # 'artist': \
                        # {
                        #     'name': item_artist_name,
                        #     'id':   item_artist_id,
                        # },
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
                elif item_type in ('Single', 'EP', 'Album'):
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
                    # print('INVALID ITEM TYPE:', item_type)
                    return # raise
            else:
                # print('INVALID ratio:', aspect_ratio)
                return # raise

            shelf_items.append(item_data)

        if not shelf_items:
            continue

        shelf_data = \
        {
            'name':      shelf_title,
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
