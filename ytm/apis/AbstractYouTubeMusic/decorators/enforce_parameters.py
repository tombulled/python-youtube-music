'''
'''

from .enforce import enforce

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

enforce_parameters = enforce \
(
    parameters   = True,
    return_value = False,
)
