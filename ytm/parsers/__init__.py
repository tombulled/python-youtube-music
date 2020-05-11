'''
Package containing parser functions
'''

from .. import utils as __utils
import types as __types

__all__ = tuple \
(
    __utils.include \
    (
        __spec__,
        lambda object: not isinstance(object, __types.ModuleType),
    ),
)
