from ..... import utils as ytm_utils
from ..search import parser as search_parser

__all__ = __name__.split('.')[-1:]

# Make decorator selfify: Parses function reference as parameter 'self'
def parse(data):
    filter = 'playlists'

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

    parsed_data = search_parser.parse(data)

    filtered_data = ytm_utils.get_nested(parsed_data, 'results', filter)

    return filtered_data
