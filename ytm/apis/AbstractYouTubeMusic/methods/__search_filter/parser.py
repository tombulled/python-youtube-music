from ... import utils
from ... import decorators
from ..search import parser as search_parser

__parser__ = __name__.split('.')[-1]
__method__ = __name__.split('.')[-2]
__all__ = (__parser__,)

@decorators.catch(__method__)
def parse(data, filter):
    assert data

    # Compat, so parser knows what each item represents
    shelves = utils.get_nested \
    (
        data,
        'contents',
        'sectionListRenderer',
        'contents',
        default = (),
    )

    assert shelves

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
