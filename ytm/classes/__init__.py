'''
Package containing classes.

These classes are used by the super package, usually as meta classes and
super classes

Example:
    >>> from ytm import classes
    >>>
    >>> classes.__all__
    ...
    >>>
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
