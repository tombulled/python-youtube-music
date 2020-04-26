from .... import utils as __utils

__inherit = __utils.include(__utils.__spec__)

locals().update(__inherit)

__all__ = \
(
    # *tuple(__inherit),
    *tuple(__utils.include(__spec__)),
)
