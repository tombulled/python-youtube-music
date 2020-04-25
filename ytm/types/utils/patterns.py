def patterns(*types, prepend=None):
    return tuple \
    (
        (prepend or '') + pattern
        for type in types
        for pattern in getattr(type, '_patterns', ())
    )
