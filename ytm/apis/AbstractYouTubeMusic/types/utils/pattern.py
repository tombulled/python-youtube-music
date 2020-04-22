__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def pattern(*segments: str) -> str:
    return '^' + ''.join(segments) + '$'
