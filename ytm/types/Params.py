from . import base
from . import utils

class Params(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.entropy \
            (
                extra  = '%',
                repeat = '+',
            ),
        ),
    )
