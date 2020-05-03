'''
Package containing utility functions.

These utility functions range in purpose, but help the super package
achieve general tasks.

Example:
    >>> utils.__all__
    ('is_float', 'parse_fflags', 'random_user_agent')
    >>>
    >>> utils.is_float('1.0')
    True
    >>>
'''

from .... import utils as __utils

locals().update(__utils.include(__utils.__spec__))

__all__ = \
(
    *tuple(__utils.include(__spec__)),
)
