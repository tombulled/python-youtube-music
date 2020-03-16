from ... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def guide(self):
    data = self.base.guide()

    scraped = \
    {
        ytm_utils.get_nested(item, 'pivotBarItemRenderer', 'title', 'runs', 0, 'text'): \
            ytm_utils.get_nested(item, 'pivotBarItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
        for item in ytm_utils.get_nested(data, 'items', 0, 'pivotBarRenderer', 'items', default = [])
    }

    return scraped
