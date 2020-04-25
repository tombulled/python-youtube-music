from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def guide(data: dict):
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

    assert pivot_items

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
