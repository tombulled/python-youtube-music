'''
Package containing utility functions.

These utility functions range in purpose, but help the super package
achieve general tasks.

Example:
    >>> from ytm.types import utils
    >>>
    >>> utils.__all__
    ...
    >>>
'''

from ... import utils as __utils

locals().update(__utils.include(__utils.__spec__))

__all__ = \
(
    *tuple(__utils.include(__spec__)),
)
