'''
'''

from ..watch import parser
from ... import decorators
from ... import constants

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.parse(parser.parse)
def method(self: object, playlist_id: str) -> dict:
    '''
    '''

    # Check playlist_id format here (e.g. preprend 'VL'?)

    return self._base.next \
    (
        playlist_id = playlist_id,
        params      = constants.PARAMS_SHUFFLE,
    )
