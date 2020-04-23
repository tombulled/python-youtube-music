__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def patterns(*types, prepend=None):
    return tuple \
    (
        (prepend or '') + pattern
        for type in types
        for pattern in getattr(type, '_patterns', ())
    )
