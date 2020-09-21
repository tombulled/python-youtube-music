'''
Module containing the decorator: _enforce
'''

import copy
import functools
import inspect
from typing import Callable, Any
from ..utils import isinstance

def _enforce(parameters: bool = True, return_value: bool = True) -> Callable:
    '''
    Enforce parameter and return value types.

    Ensure arguments passed to a function and the function return value are of
    the type specified by the function type hints

    Args:
        parameters: Whether to enforce arguments types
        return_value: Whether to enforce the return value type

    Returns:
        The enforcing decorator

    Example:
        >>> @_enforce()
        def foo(x: int) -> str:
        	return 'It worked!'
        >>>
        >>> # Acceptable
        >>> foo(1)
        'It worked!'
        >>>
        >>> # Unacceptable
        >>> foo('a')
        TypeError: Expected argument 'x' to be of type 'int' not 'str'
        >>>
    '''

    enforce_parameters = parameters
    enforce_return     = return_value

    def decorator(func: Callable) -> Callable:
        '''
        Decorate func to enforce types.

        Args:
            func: Function to decorate

        Returns:
            The decorated func
        '''

        signature = inspect.signature(func)

        is_empty = lambda object: getattr(object, '__name__', None) == inspect._empty.__name__

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            '''
            Wrap func to enforce types as previously specified

            Args:
                *args: Function arguments
                **kwargs: Function keyword arguments

            Returns:
                The wrapped functions return value
            '''

            parameters = signature.parameters \
                if enforce_parameters \
                else {}

            arguments = copy.deepcopy(kwargs)

            for index, (parameter_name, parameter) in enumerate(parameters.items()):
                if parameter_name in arguments:
                    continue

                if parameter.kind == parameter.VAR_POSITIONAL:
                    arguments[parameter_name] = args[index:]

                    break
                elif index < len(args):
                    arguments[parameter_name] = args[index]

            for parameter_name, parameter in parameters.items() \
                    if parameters else ():
                parameter_annotation = parameter.annotation
                parameter_annotation_name = parameter_annotation.__name__ \
                    if isinstance(parameter_annotation, type) \
                    else repr(parameter_annotation)
                parameter_default = parameter.default
                parameter_value = arguments.get(parameter_name)
                parameter_type = type(parameter_value)
                parameter_type_name = parameter_type.__name__

                if parameter_name not in arguments:
                    if not is_empty(parameter_default):
                        continue
                    else:
                        raise TypeError \
                        (
                            f'Missing argument: '
                            f'{repr(parameter_name)}'
                        )

                if not is_empty(parameter_annotation) \
                        and parameter_value != parameter_default:
                    if parameter.kind == parameter.VAR_POSITIONAL:
                        for item in parameter_value:
                            parameter_item_type = type(item)

                            if not isinstance(item, parameter_annotation):
                                raise TypeError \
                                (
                                    f'Expected argument '
                                    f'{repr(parameter_name)} to all be of type '
                                    f'{repr(parameter_annotation_name)} not contain '
                                    f'{repr(parameter_item_type)}'
                                )
                    elif not isinstance(parameter_value, parameter_annotation):
                        raise TypeError \
                        (
                            f'Expected argument '
                            f'{repr(parameter_name)} to be of type '
                            f'{repr(parameter_annotation_name)} not '
                            f'{repr(parameter_type_name)}'
                        )

            resp = func(*args, **kwargs)

            if enforce_return \
                    and not is_empty(signature.return_annotation) \
                    and not isinstance(resp, signature.return_annotation):
                raise TypeError \
                (
                    f'Expected return value to be of type '
                    f'{repr(signature.return_annotation.__name__)} not '
                    f'{repr(resp.__class__.__name__)}'
                )

            return resp

        return wrapper

    return decorator
