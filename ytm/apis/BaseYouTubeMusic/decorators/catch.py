'''
'''

import functools
from .. import exceptions
import requests.exceptions
import urllib3.exceptions

def catch(func):
    '''
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''
        '''

        exception = None
        exception_message = None

        try:
            resp = func(*args, **kwargs)
        except requests.exceptions.ConnectionError as error:
            # Use str(error) instead ??
            argument = error.args[0]

            # import sys
            # sys._x = argument

            if isinstance(argument, str):
                exception_message = argument
            elif isinstance(argument, urllib3.exceptions.MaxRetryError):
                error_name = argument.__class__.__name__

                pool = argument.pool
                reason = argument.reason
                endpoint = argument.url

                host = pool.host
                port = pool.port
                protocol = pool.scheme

                reason_message = reason.args[0].split(':', 2)[1].strip()

                url = f'{protocol}://{host}:{port}{endpoint}'

                exception_message = f'{error_name} - {reason_message} ({repr(url)})'
            elif isinstance(argument, urllib3.exceptions.ProtocolError):
                error_name = argument.__class__.__name__
                error_message = argument.args[0]

                exception_message = f'{error_name} - {error_message}'
            else:
                exception_message = str(error)

            exception = exceptions.ConnectionError

        if exception:
            raise exception(exception_message)

        if isinstance(resp, dict):
            if 'error' in resp:
                raise exceptions.YouTubeMusicApiError(resp)
            if 'errorcode' in resp:
                raise exceptions.YouTubeApiError(resp)

        return resp

    return wrapper
