'''
Module containing the decorator: catch
'''

import functools
import requests.exceptions
import urllib3.exceptions
from .... import exceptions

def catch(func):
    '''
    Catch method errors and re-raise them appropriately.

    Methods can raise exceptions when something goes wrong,
    this decorator re-raises them.

    Args:
        func: Function to decorate

    Returns:
        Decorated func

    Raises:
        ConnectionError: Failed to connect to host
        YouTubeMusicApiError: YouTube Music Api Error
        YouTubeApiError: YouTube Api Error
        MethodError: Method encountered an error

    Example:
        >>> @catch
        def foo():
        	raise Exception('An error occured!')

        >>> foo()
        MethodError: An error occured!
        >>>
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''
        Wrap func to re-raise exceptions.

        Args:
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            The wrapped functions return value
        '''

        exception = None
        exception_message = None

        try:
            resp = func(*args, **kwargs)
        except requests.exceptions.ConnectionError as error:
            argument = error.args[0]

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
        except TimeoutError as error:
            error_name = error.__class__.__name__

            error_number = error.errno
            error_message = error.strerror

            exception_message = f'{error_name} - [{error_number}] {error_message}'

            exception = exceptions.ConnectionError
        except Exception as error:
            exception_message = str(error)

            exception = exceptions.MethodError

        if exception:
            raise exception(exception_message)

        if isinstance(resp, dict):
            if 'error' in resp:
                raise exceptions.YouTubeMusicApiError(resp)
            if 'errorcode' in resp:
                raise exceptions.YouTubeApiError(resp)

        return resp

    return wrapper
