'''
'''

import functools
from .. import exceptions

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def catch(func):
    '''
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''
        '''

        resp = func(*args, **kwargs)

        if isinstance(resp, dict):
            if 'error' in resp:
                raise exceptions.YouTubeMusicApiError(resp)
            if 'errorcode' in resp:
                raise exceptions.YouTubeApiError(resp)

        return resp

    return wrapper
