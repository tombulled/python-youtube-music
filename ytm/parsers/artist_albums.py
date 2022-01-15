'''
Module containing the parser: artist_albums
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def artist_albums(data: dict) -> list:
    '''
    Parse data: Artist Albums

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
        >>> albums_params = artist['albums']['params']
        >>>
        >>> data = api.browse(artist_id, params=albums_params)
        >>>
        >>> parsed_data = ytm.parsers.artist_albums(data)
        >>>
        >>> parsed_data[0]['name']
        'Wonderland (Deluxe)'
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
        default = (),
    )

    assert contents, 'Data has no contents'

    albums_data = []

    for item in contents:
        item = utils.get \
        (
            item,
            'musicResponsiveListItemRenderer',
        )

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

            # Change this to use camel-case, then update the extractors
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
        item_flex_column_0_runs = utils.get \
        (
            item,
            'flexColumns',
            0,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
        )
        item_flex_column_1_runs = utils.get \
        (
            item,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
        )

        item_album_page_type = utils.get \
        (
            item_browse_endpoint,
            'browseEndpointContextSupportedConfigs',
            'browseEndpointContextMusicConfig',
            'pageType',
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
        item_album_id = utils.get \
        (
            item_browse_endpoint,
            'browseId',
        )
        item_album_params = utils.get \
        (
            item_browse_endpoint,
            'params',
        )
        item_album_name = utils.get \
        (
            item_flex_column_0_runs,
            0,
            'text',
        )
        item_type = utils.get \
        (
            item_flex_column_1_runs,
            0,
            'text',
        )
        item_year = utils.get \
        (
            item_flex_column_1_runs,
            2,
            'text',
            func = int,
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
            'name':      item_album_name,
            'id':        item_album_id,
            'type':      item_type,
            'year':      item_year,
            'explicit':  item_explicit,
            # 'params':    item_album_params,
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

        albums_data.append(item_data)

    return albums_data
