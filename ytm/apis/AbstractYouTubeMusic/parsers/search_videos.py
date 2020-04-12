from .... import utils as ytm_utils
from .search import search as parse_search

__all__ = __name__.split('.')[-1:]

# Make decorator selfify: Parses function reference as parameter 'self'
def search_videos(data):
    filter = 'videos'

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

    parsed_data = parse_search(data)

    filtered_data = ytm_utils.get_nested(parsed_data, 'results', filter)

    return filtered_data
