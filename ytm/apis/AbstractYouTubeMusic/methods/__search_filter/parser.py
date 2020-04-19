from ... import utils
from ..search import parser as search_parser

__parser__ = __name__.split('.')[-1]
__all__ = (__parser__,)

def parse(data, filter):
    # Compat, so parser knows what each item represents
    shelves = utils.get_nested(data, 'contents', 'sectionListRenderer', 'contents', default=())

    for shelf in shelves:
        shelf = utils.first_key(shelf)

        shelf['title'] = \
        {
            'runs': \
            [
                {
                    'text': filter.title(),
                },
            ],
        }

    parsed_data = search_parser.parse(data)

    filtered_data = utils.get_nested(parsed_data, filter)

    return filtered_data
