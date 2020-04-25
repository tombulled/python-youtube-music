from .. import utils
from . import decorators
from .search import search as parse_search

@decorators.enforce_parameters
@decorators.catch
def _search_filter(data: dict, filter: str):
    assert data, 'No data to parse'

    shelves = utils.get \
    (
        data,
        'contents',
        'sectionListRenderer',
        'contents',
        default = (),
    )

    assert shelves, 'No search results found'

    for shelf in shelves:
        shelf = utils.first(shelf)

        shelf['title'] = \
        {
            'runs': \
            [
                {
                    'text': filter.title(),
                },
            ],
        }

    parsed_data = parse_search(data)

    filtered_data = utils.get(parsed_data, filter)

    return filtered_data
