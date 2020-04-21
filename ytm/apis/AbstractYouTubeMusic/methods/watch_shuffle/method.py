'''
'''

from ..watch import parser
from ... import decorators
from ... import constants
from ...types import SongListId

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, playlist_id: SongListId) -> dict:
    '''
    '''

    # Check playlist_id format here (e.g. preprend 'VL'?)

    return self._base.next \
    (
        playlist_id = playlist_id,
        params      = constants.PARAMS_SHUFFLE,
    )
