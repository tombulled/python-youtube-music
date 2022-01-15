'''
Module containing the parser: search_suggestions
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_suggestions(data: dict) -> list:
    '''
    Parse data: Search Suggestions.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.search_suggestions('band of')
        >>>
        >>> parsed_data = ytm.parsers.search_suggestions(data)
        >>>
        >>> for suggestion in parsed_data:
        	print(suggestion)

        band of horses the funeral
        band of horses
        band of heathens hurricane
        band of gold
        band of brothers theme
        band of boys
        band of horses no one's gonna love you
        >>>
    '''

    assert data, 'No data to parse'

    contents = utils.get \
    (
        data,
        'contents',
        0,
        'searchSuggestionsSectionRenderer',
        'contents',
        default = (),
    )

    assert contents, 'No contents'

    suggestions = []

    for item in contents:
        item_runs = utils.get \
        (
            item,
            'searchSuggestionRenderer',
            'suggestion',
            'runs',
            default = (),
        )

        if not item_runs:
            continue

        item_suggestion = ''

        for item_run in item_runs:
            item_run_text = utils.get \
            (
                item_run,
                'text',
            )

            if item_run_text:
                item_suggestion += item_run_text

        if item_suggestion:
            suggestions.append(item_suggestion)

    return suggestions
