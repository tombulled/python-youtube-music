'''
Module containing the decorator: catch
'''

from ... import exceptions

import functools
from typing import Callable, Any

def catch(func: Callable) -> Callable:
    '''
    Catch and re-raise errors encountered during parsing.

    Args:
        func: Parser to decorate

    Returns:
        Decorated function

    Example:
        >>> @catch
        def my_parser(data: dict) -> dict:
        	assert 'age' in data, 'Data has no age'
        	return data

        >>>
        >>> my_parser({'age': 12})
        {'age': 12}
        >>>
        >>> my_parser({'name': 'Foo'})
        ParserError: my_parser() encountered an error: Data has no age
        >>>
        >>>
    '''

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        '''
        Wrap {func} to re-raise any exceptions

        Args:
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            Function return value
        '''

        try:
            return func(*args, **kwargs)
        except exceptions.ParserError as error:
            error_message = f'{error.parser}() - {error.message}'
        except Exception as error:
            error_message = str(error) or 'Unknown'

        raise exceptions.ParserError \
        (
            parser  = func.__name__,
            message = error_message,
        )

    return wrapper
