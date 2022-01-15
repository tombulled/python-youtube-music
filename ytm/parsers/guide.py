'''
Module containing the parser: guide
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def guide(data: dict) -> dict:
    '''
    Parse data: Guide.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.guide()
        >>>
        >>> parsed_data = ytm.parsers.guide(data)
        >>>
        >>> parsed_data['Home']
        'FEmusic_home'
        >>>
    '''

    assert data, 'No data to parse'

    scraped = {}

    pivot_items = utils.get \
    (
        data,
        'items',
        0,
        'pivotBarRenderer',
        'items',
        default = (),
    )

    assert pivot_items, 'Data has no pivot items'

    for pivot_item in pivot_items:
        pivot_item = utils.get \
        (
            pivot_item,
            'pivotBarItemRenderer',
        )

        pivot_item_title = utils.get \
        (
            pivot_item,
            'title',
            'runs',
            0,
            'text',
        )
        pivot_item_browse_id = utils.get \
        (
            pivot_item,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )

        scraped[pivot_item_title] = pivot_item_browse_id

    return scraped
