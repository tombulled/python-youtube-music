'''
'''

import functools
from typing import Callable, Any
import inspect
from .. import types

__decorator__ = __name__.split('.')[-1]
__all__       = (__decorator__,)

def enforce(parameters: bool = True, return_value: bool = True):
    enforce_parameters = parameters
    enforce_return = return_value

    def decorator(func: Callable):
        signature = inspect.signature(func)
        argument_keys = list(signature.parameters)

        is_empty = lambda object: getattr(object, '__name__', None) == inspect._empty.__name__

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            arguments = {**dict(zip(argument_keys, args)), **kwargs}

            # print(arguments)

            parameters = signature.parameters \
                if enforce_parameters \
                else {}

            for parameter_name, parameter in parameters.items() \
                    if parameters else ():
                parameter_annotation = parameter.annotation
                parameter_annotation_name = parameter_annotation.__name__
                parameter_default = parameter.default
                parameter_value = arguments.get(parameter_name)
                parameter_type = type(parameter_value)
                parameter_type_name = parameter_type.__name__

                # print(parameter_default)

                if parameter_name not in arguments:
                    if not is_empty(parameter_default):
                        continue
                    else:
                        raise TypeError \
                        (
                            f'{func.__name__}() missing argument: '
                            f'{repr(parameter_name)}'
                        )

                # if not is_empty(parameter_default) \
                #         and parameter_name not in arguments:
                #         # and parameter_name in arguments \
                #         # and parameter_value == parameter_default:
                #     continue
                #
                # if parameter_name not in arguments:
                #     raise TypeError \
                #     (
                #         f'{func.__name__}() missing argument: '
                #         f'{repr(parameter_name)}'
                #     )

                # parameter_value = arguments[parameter_name]
                # parameter_type = type(parameter_value)
                # parameter_type_name = parameter_type.__name__

                if not is_empty(parameter_annotation) \
                        and not types.isinstance(parameter_value, parameter_annotation):
                    raise TypeError \
                    (
                        f'{func.__name__}() expected parameter '
                        f'{repr(parameter_name)} to be of type '
                        f'{repr(parameter_annotation_name)} not '
                        f'{repr(parameter_type_name)}'
                    )

            resp = func(*args, **kwargs)

            if enforce_return \
                    and not is_empty(signature.return_annotation) \
                    and not types.isinstance(resp, signature.return_annotation):
                raise TypeError \
                (
                    f'{func.__name__}() expected return value to be of type '
                    f'{repr(signature.return_annotation.__name__)} not '
                    f'{repr(resp.__class__.__name__)}'
                )

            return resp

        return wrapper

    return decorator
