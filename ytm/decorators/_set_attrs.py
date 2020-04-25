import functools
from typing import Callable, Any

def _set_attrs(attrs: dict):
    def decorator(func):
        for key, val in attrs.items():
            setattr(func, key, val)

        return func

    return decorator
