'''
'''

import functools
from typing import Callable, Any
from ... import exceptions

def catch(func: Callable):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        try:
            return func(*args, **kwargs)
        except exceptions.ParserError as error:
            error_message = f'{error.parser}() - {error.message}'
        except Exception as error:
            error_message = str(error) or 'Unknown'

        raise exceptions.ParserError \
        (
            parser = func.__name__,
            message = error_message,
        )

    return wrapper
