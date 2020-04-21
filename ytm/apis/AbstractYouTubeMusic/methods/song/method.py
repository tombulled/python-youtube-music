from . import parser
from ... import decorators

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.enforce(parameters=False, return_value=True)
@decorators.parse(parser.parse)
@decorators.enforce(parameters=True, return_value=False)
@decorators.rename(__method__)
def method(self: object, song_id) -> dict:
    return self._base.video_info \
    (
        video_id = song_id,
    )
