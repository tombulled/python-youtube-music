'''
Package containing base types.

These types form the base of other types and carry out core functionality.

Example:
    >>> from ytm.types import base
    >>>
    >>> base.__all__
    ...
    >>>
'''

from ...utils import include as __include

__all__ = tuple(__include(__spec__))
