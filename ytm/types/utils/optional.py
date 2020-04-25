def optional(*values):
    return '({values})?'.format \
    (
        values = '|'.join(values),
    )
