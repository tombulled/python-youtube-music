'''
Module containing the parser: watch_shuffle
'''

from .watch import watch as parse_watch
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def watch_shuffle(data: dict):
    '''
    Parse data: Watch Shuffle.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.next \
        (
        	playlist_id = 'RDCLAK5uy_kzInc7BXjYqbrGEiqW9fBhOZoroJvfsao',
        	params      = ytm.constants.PARAMS_SHUFFLE,
        )
        >>>
        >>> parsed_data = ytm.parsers.watch_shuffle(data)
        >>>
        >>> parsed_data['tracks'][0]['name']
        'California Gurls (feat. Snoop Dogg)'
        >>>
    '''

    return parse_watch(data)
