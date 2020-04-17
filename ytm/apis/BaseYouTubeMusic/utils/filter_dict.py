__all__ = __name__.split('.')[-1:]

def filter_dict(dictionary, func=None):
    if func is None:
        func = lambda key, val: val is not None

    return \
    {
        key: val
        for key, val in dictionary.items()
        if func(key, val)
    }
