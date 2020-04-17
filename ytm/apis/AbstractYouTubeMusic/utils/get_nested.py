from .iter_get import iter_get

__all__ = __name__.split('.')[-1:]

def get_nested(data, *keys, default=None, func=None):
    if not keys or not data: return default

    for key in keys[:-1]:
        data = iter_get(data, key, {})

    if not data:
        return default

    item = iter_get(data, keys[-1], default=default)

    if func and item != default:
        item = func(item)

    return item
