__all__ = __name__.split('.')[-1:]

def iter_get(iterable, key, default=None):
    if not iterable: return default

    try:
        return iterable.__getitem__(key)
    except (KeyError, IndexError):
        return default
