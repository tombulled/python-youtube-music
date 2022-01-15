'''
Package containing utility functions.

These utility functions range in purpose, but help the super package
achieve general tasks.

Example:
    >>> from ytm import utils
    >>>
    >>> utils.__all__
    ...
    >>>
'''

from .include import include as __include

__all__ = tuple(__include(__spec__))
