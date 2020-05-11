'''
Module containing the parser: watch_radio
'''

from .watch import watch as parse_watch
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def watch_radio(data: dict) -> dict:
    '''
    Parse data: Watch Radio.

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
        	params      = ytm.constants.PARAMS_RADIO,
        )
        >>>
        >>> parsed_data = ytm.parsers.watch_radio(data)
        >>>
        >>> parsed_data['tracks'][0]['name']
        'My Humps'
        >>>
    '''

    return parse_watch(data)
