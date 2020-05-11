'''
Package containing decorators.
'''

from ... import \
(
    utils as __utils,
    decorators as __decorators,
)

__inherit = __utils.include(__decorators.__spec__)

locals().update(__inherit)

__all__ = \
(
    *tuple(__utils.include(__spec__)),
)
