'''
Module containing the parser: _search_filter
'''

from .. import utils
from . import decorators
from ._search import _search as parse_search

@decorators.enforce_parameters
@decorators.catch
def _search_filter(data: dict, filter: str) -> dict:
    '''
    Parse filtered search data.

    Args:
        data: Data to parse
        filter: Search filter
            Example: 'artists'

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> params_artists = ytm.constants.SEARCH_PARAM_PREFIX  \
        		           + ytm.constants.SEARCH_PARAM_ARTISTS \
        		           + ytm.constants.SEARCH_PARAM_SUFFIX
        >>>
        >>> data = api.search('foo fighters', params = params_artists)
        >>>
        >>> parsed_data = ytm.parsers._search_filter(data, 'artists')
        >>>
        >>> parsed_data['items'][0]['name']
        'Foo Fighters'
        >>>
    '''

    assert data, 'No data to parse'

    if 'continuationContents' in data:
        shelf = utils.get \
        (
            data,
            'continuationContents',
            'musicShelfContinuation',
            default = (),
        )

        assert shelf, 'Invalid continuation data'

        shelves = (shelf,)

        data['contents'] = \
        {
            'tabbedSearchResultsRenderer': \
            {
                'tabs': \
                [
                    {
                        'tabRenderer': \
                        {
                            'content': \
                            {
                                'sectionListRenderer': \
                                {
                                    'contents': \
                                    (
                                        {
                                            'musicShelfRenderer': \
                                            {
                                                **shelf,
                                            },
                                        },
                                    ),
                                },
                            },
                        },
                    },
                ],
            },
        }

    shelves = utils.get \
    (
        data,
        'contents',
        'tabbedSearchResultsRenderer',
        'tabs',
        0,
        'tabRenderer',
        'content',
        'sectionListRenderer',
        'contents',
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

    parsed_data   = parse_search(data)
    filtered_data = utils.get(parsed_data, filter)

    return filtered_data
