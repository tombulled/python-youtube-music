from ..... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def _parse(self):
    scraped = {}

    pivot_items = ytm_utils.get_nested(self.raw_data, 'items', 0, 'pivotBarRenderer', 'items', default = [])

    for pivot_item in pivot_items:
        title = ytm_utils.get_nested(pivot_item, 'pivotBarItemRenderer', 'title', 'runs', 0, 'text')
        browse_id = ytm_utils.get_nested(pivot_item, 'pivotBarItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')

        scraped[title] = browse_id

    return scraped
