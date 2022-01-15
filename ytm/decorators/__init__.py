'''
Package containing decorators.

These decorators range in purpose, but help the super package
achieve general tasks.

Example:
    >>> from ytm import decorators
    >>>
    >>> decorators.__all__
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
        lambda object: not isinstance(object, __types.ModuleType) \
            and not object.__name__.startswith('_'),
    ),
)
