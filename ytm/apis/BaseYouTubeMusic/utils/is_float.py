import re

__all__ = __name__.split('.')[-1:]

def is_float(string: str) -> bool:
    return re.match(r'^\d+\.\d+$', string.strip()) is not None
