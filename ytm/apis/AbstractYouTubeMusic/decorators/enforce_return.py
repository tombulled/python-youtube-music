'''
'''

import functools
from .enforce import enforce

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

enforce_return = enforce \
(
    parameters   = False,
    return_value = True,
)

# def enforce_return(func):
#     @functools.wraps(func)
#     @enforce \
#     (
#         parameters   = False,
#         return_value = True,
#     )
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return wrapper
