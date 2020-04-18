'''
'''

from . import utils
from . import decorators

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.staticmethod
def _url_yt(endpoint: str = None) -> str:
    '''
    '''

    return utils.url_youtube \
    (
        endpoint = endpoint or '',
    )
