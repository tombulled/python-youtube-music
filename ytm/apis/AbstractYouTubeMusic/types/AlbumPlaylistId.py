from .BaseType import BaseType
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class AlbumPlaylistId(BaseType):
    # Alow and left-strip RDAMPL
    
    _patterns = \
    (
        utils.pattern \
        (
            'OLAK5uy_',
            utils.entropy(33),
        ),
    )
