'''
Package containing exception classes.

These exceptions are used by the super package to raise appropriate errors

Example:
    >>> from ytm import exceptions
    >>>
    >>> exceptions.__all__
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
