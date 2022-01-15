'''
Module containing the parser: artist_singles
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def artist_singles(data: dict) -> list:
    '''
    Parse data: Artist Singles

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api_base     = ytm.BaseYouTubeMusic()
        >>> api_abstract = ytm.AbstractYouTubeMusic()
        >>>
        >>> artist_id = 'UCTK1maAvqrDlD2agZDGZzjw' # Take That
        >>>
        >>> artist = api_abstract.artist(artist_id)
        >>>
        >>> singles_params = artist['singles']['params']
        >>>
        >>> data = api.browse(artist_id, params=singles_params)
        >>>
        >>> parsed_data = ytm.parsers.artist_singles(data)
        >>>
        >>> parsed_data[0]['name']
        'Cry (Live)'
        >>>
    '''

    assert data, 'No data to parse'

    header = utils.get \
    (
        data,
        'header',
        'musicHeaderRenderer',
    )

    assert header, 'Data has no header'

    contents = utils.get \
    (
        data,
        'contents',
        'singleColumnBrowseResultsRenderer',
        'tabs',
        0,
        'tabRenderer',
        'content',
        'sectionListRenderer',
        'contents',
        0,
        'musicShelfRenderer',
        'contents',
    )

    assert contents, 'Data has no contents'

    parsed_items = []

    for item in contents:
        item = utils.first(item)

        # return item

        item_menu_items = utils.get \
        (
            item,
            'menu',
            'menuRenderer',
            'items',
            default = (),
        )

        item_menu_items_map = {}

        for item_menu_item in item_menu_items:
            item_menu_item = utils.first(item_menu_item)

            item_menu_item_text = utils.get \
            (
                item_menu_item,
                'text',
                'runs',
                0,
                'text',
            )

            if not item_menu_item_text:
                item_menu_item_text = utils.get \
                (
                    item_menu_item,
                    'defaultText',
                    'runs',
                    0,
                    'text',
                )

            if not item_menu_item_text:
                return # raise

            # Use camel-case instead and update extractors
            item_menu_item_identifier = item_menu_item_text.strip().lower().replace(' ', '_')

            item_menu_items_map[item_menu_item_identifier] = item_menu_item

        item_badges = utils.get \
        (
            item,
            'badges',
            default = (),
        )

        item_badges_map = {}

        for badge in item_badges:
            badge = utils.first(badge)

            badge_label = utils.get \
            (
                badge,
                'accessibilityData',
                'accessibilityData',
                'label',
            )

            if not badge_label:
                return # raise/log

            # Use camel-case istead
            badge_identifier = badge_label.strip().lower().replace(' ', '_')

            item_badges_map[badge_identifier] = badge

        item_browse_endpoint = utils.get \
        (
            item,
            'navigationEndpoint',
            'browseEndpoint',
        )
        item_shuffle_playlist_endpoint = utils.get \
        (
            item_menu_items_map,
            'shuffle_play',
            'navigationEndpoint',
            'watchPlaylistEndpoint',
        )
        item_radio_playlist_endpoint = utils.get \
        (
            item_menu_items_map,
            'start_radio',
            'navigationEndpoint',
            'watchPlaylistEndpoint',
        )

        item_id = utils.get \
        (
            item_browse_endpoint,
            'browseId',
        )
        item_params = utils.get \
        (
            item_browse_endpoint,
            'params',
        )
        item_name = utils.get \
        (
            item,
            'flexColumns',
            0,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
        )
        item_year = utils.get \
        (
            item,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
            func = int,
        )
        item_thumbnail = utils.get \
        (
            item,
            'thumbnail',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        item_shuffle_playlist_params = utils.get \
        (
            item_shuffle_playlist_endpoint,
            'params',
        )
        item_shuffle_playlist_id = utils.get \
        (
            item_shuffle_playlist_endpoint,
            'playlistId',
        )
        item_radio_playlist_params = utils.get \
        (
            item_radio_playlist_endpoint,
            'params',
        )
        item_radio_playlist_id = utils.get \
        (
            item_radio_playlist_endpoint,
            'playlistId',
        )

        item_explicit = 'explicit' in item_badges_map

        item_data = \
        {
            'name':      item_name,
            'id':        item_id,
            'year':      item_year,
            'explicit':  item_explicit,
            # 'params':    item_params,
            'thumbnail': item_thumbnail,
            'shuffle': \
            {
                'params':      item_shuffle_playlist_params,
                'playlist_id': item_shuffle_playlist_id,
            },
            'radio': \
            {
                'params':      item_radio_playlist_params,
                'playlist_id': item_radio_playlist_id,
            },
        }

        parsed_items.append(item_data)

    return parsed_items
