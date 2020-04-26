from . import base
from . import utils

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
