from ... import utils

__parser__ = __name__.split('.')[-1]
__all__ = (__parser__,)

def parse(data):
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
