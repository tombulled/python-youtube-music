__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def group(name: str) -> str:
    return f'(?P={name})'
