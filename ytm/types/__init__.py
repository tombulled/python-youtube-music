'''
Package containing type classes.
'''

from ..utils import include as __include
from . import \
(
    base,
    continuations,
    ids,
    params,
)

__inherit = \
(
    base,
    continuations,
    ids,
    params,
)

locals().update \
(
    {
        key: val
        for spec in \
        (
            __spec__,
            * \
            (
                getattr(module, '__spec__')
                for module in __inherit
            ),
        )
        for key, val in __include(spec).items()
    }
)

__all__ = tuple \
(
    item
    for module in __inherit
    for item in getattr(module, '__all__')
)
