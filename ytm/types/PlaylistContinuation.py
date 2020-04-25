from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistContinuation(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            '4qmFsgJbEi1WTFJEQ0xBSzV1eV9',
            utils.entropy(45),
            'KmVoVlFWRHBGWjN',
            utils.entropy(28),
            'TQVFNSXVnUSUzRA%3D%3D',
        ),
    )
