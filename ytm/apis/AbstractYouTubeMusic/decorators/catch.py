'''
'''

import functools
from typing import Callable, Any
from .. import exceptions

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def catch(method_name):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            # error_message = None
            resp = None
            error = None

            # print(error)

            try:
                resp = func(*args, **kwargs)
            except Exception as _error:
                error = _error
                # print(error)
                # pass

            # print(error)

            # if resp is None:
            if error is not None:
                # raise exceptions.InvalidResponseError \
                # (
                #     f'Invalid response when parsing for method {repr(method_name)}',
                # )
                error_message = f'{method_name}() encountered error'

                # print(error, error.args)

                if error.args:
                    error_message += f': {error.args[0]}'

                raise Exception(error_message)

            return resp

        return wrapper

    return decorator
