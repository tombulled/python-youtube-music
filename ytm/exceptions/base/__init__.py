'''
Package containing base exception classes.

These base exceptions are used by derived exceptions to inherit core
functionality

Example:
    >>> from ytm.exceptions import base
    >>>
    >>> base.__all__
    ...
    >>>
'''

from ... import utils as __utils
import types as __types

__all__ = tuple \
(
    __utils.include \
    (
        __spec__,
        lambda object: not isinstance(object, __types.ModuleType),
    ),
)
