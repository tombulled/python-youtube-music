__all__ = __name__.split('.')[-1:]

def filter_dict(dictionary, func=bool):
    return \
    {
        key: val
        for key, val in dictionary.items()
        if func(key, val)
    }
