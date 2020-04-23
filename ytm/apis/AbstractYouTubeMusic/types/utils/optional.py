__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def optional(*values):
    return '({values})?'.format \
    (
        values = '|'.format(values),
    )
