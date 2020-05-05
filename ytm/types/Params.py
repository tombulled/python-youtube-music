from . import base
from . import utils
from . import constants

class Params(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.entropy \
            (
                chars  = constants.CHARS_PARAM,
                repeat = '+',
            ),
        ),
    )
