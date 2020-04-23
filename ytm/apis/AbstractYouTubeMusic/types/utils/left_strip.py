__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def left_strip(data, value):
    if data.startswith(value):
        data = data[len(value):]

    return data
