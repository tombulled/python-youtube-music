__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def entropy(length: int = None, extra: str = None, name: str = None, repeat: str = None) -> str:
    # repeat: '+' or '*' etc.
    return '({prefix}[-a-zA-Z0-9_{extra}]{{{length}}}){repeat}'.format \
    (
        prefix = f'?P<{name}>' if name else '',
        extra  = extra or '',
        length = length or 1,
        repeat = repeat or ''
    )
