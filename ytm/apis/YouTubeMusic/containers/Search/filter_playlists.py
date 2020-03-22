from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def filter_playlists(self, update=True):
    filter = 'playlists'
    params = ytm_utils.get_nested(self, 'results', filter, 'params')
    items = ytm_utils.get_nested(self, 'results', filter, 'items', default=[])
    query = ytm_utils.get_nested(self, 'query')

    if not params or not query: return # raise

    data = self.api.base.search \
    (
        query = query,
        params = params,
    )

    # Compat, so parser knows what each item represents
    shelves = ytm_utils.get_nested(data, 'contents', 'sectionListRenderer', 'contents', default=())

    for shelf in shelves:
        shelf['musicShelfRenderer']['title'] = \
        {
            'runs': \
            [
                {
                    'text': filter.title(),
                },
            ],
        }

    parsed_data = self._parse(data)

    # parsed_data['query'] = query

    filtered_data = ytm_utils.get_nested(parsed_data, 'results', filter)
    filtered_items = ytm_utils.get_nested(filtered_data, 'items')

    # filtered_data['params'] = params

    parsed_items = ytm_utils.get_nested(parsed_data, 'results', filter, 'items', default=[])

    if update and items:
        items.extend(parsed_items[len(items):])

    container = containers.SearchPlaylists(self.api, filtered_data)

    container._continuation = ytm_utils.get_nested(filtered_data, 'continuation')

    return container
