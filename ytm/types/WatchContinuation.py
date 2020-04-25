from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class WatchContinuation(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'CBkSMRIL',
            utils.entropy(15),
            'iEVJEQU1WT',
            utils.entropy(15),
            'MgR3QUVCOBi4AQLQAQHwAQEYCg%3D%3D',
        ),
    )
