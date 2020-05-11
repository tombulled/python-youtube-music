'''
Module containing the parser: search
'''

from ._search import _search as parse_search
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search(data: dict) -> dict:
    '''
    Parse data: Search.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.search('bears den')
        >>> 
        >>> parsed_data = ytm.parsers.search(data)
        >>>
        >>> parsed_data['artists'][0]['name']
        "Bear's Den"
        >>>
    '''

    parsed = parse_search(data)

    for shelf_name, shelf in parsed.items():
        if 'items' in shelf:
            parsed[shelf_name] = shelf.get('items')

    return parsed
