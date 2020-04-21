'''
'''

from ..watch import parser
from ... import decorators
from ... import constants

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.enforce(parameters=False, return_value=True)
@decorators.parse(parser.parse)
@decorators.enforce(parameters=True, return_value=False)
@decorators.rename(__method__)
def method(self: object, playlist_id: str) -> dict:
    '''
    '''

    # Check playlist_id format here (e.g. preprend 'VL'?)

    return self._base.next \
    (
        playlist_id = playlist_id,
        params      = constants.PARAMS_SHUFFLE,
    )
