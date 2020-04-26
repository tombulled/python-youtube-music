from typing import Callable

def _set_attrs(attrs: dict) -> Callable:
    def decorator(func: Callable) -> Callable:
        for key, val in attrs.items():
            setattr(func, key, val)

        return func

    return decorator
