__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def patterns(*types):
    return tuple \
    (
        pattern
        for type in types
        for pattern in getattr(type, '_patterns', ())
    )
