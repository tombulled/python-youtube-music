import builtins

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def isinstance(object, class_):
    if builtins.isinstance(object, class_):
        return True

    return getattr(class_, '_validate', lambda object: False)(object)
