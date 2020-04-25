'''
'''

# from .watch import watch as parse_watch
from .. import parsers
from .. import decorators
from .. import constants
from ..types import SongListId

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.watch_radio)
def watch_radio(self: object, playlist_id: SongListId) -> dict:
    '''
    '''

    # Check playlist_id format here (e.g. preprend 'VL'?)

    return self._base.next \
    (
        playlist_id = playlist_id,
        params      = constants.PARAMS_RADIO,
    )
