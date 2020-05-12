'''
Module containing the utility function: pad_base64
'''

def pad_base64(data: str) -> bool:
    '''
    Pad some base64 data.

    Args:
        data: Data to pad

    Returns:
        Padded data

    Example:
        >>> pad_base64('foo')
        'foo='
        >>> pad_base64('abcdabcd')
        'abcdabcd'
        >>>
    '''

    mod = len(data) % 4

    if mod:
        data += '=' * (4 - mod)

    return data
