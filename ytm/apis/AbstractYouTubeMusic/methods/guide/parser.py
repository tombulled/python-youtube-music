from ... import utils
from ... import decorators

__parser__ = __name__.split('.')[-1]
__method__ = __name__.split('.')[-2]
__all__ = (__parser__,)

@decorators.catch(__method__)
def parse(data):
    assert data
    
    scraped = {}

    pivot_items = utils.get_nested \
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
        pivot_item = utils.get_nested \
        (
            pivot_item,
            'pivotBarItemRenderer',
        )

        pivot_item_title = utils.get_nested \
        (
            pivot_item,
            'title',
            'runs',
            0,
            'text',
        )
        pivot_item_browse_id = utils.get_nested \
        (
            pivot_item,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )

        scraped[pivot_item_title] = pivot_item_browse_id

    return scraped
