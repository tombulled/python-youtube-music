import builtins

def isinstance(object, class_):
    return builtins.isinstance(object, class_) \
        or getattr(class_, '_validate', lambda object: False)(object)
