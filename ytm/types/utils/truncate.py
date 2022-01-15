'''
Module containing the utility function: truncate
'''

def truncate(string: str, length: int = 50, suffix: str = '...') -> str:
    '''
    Truncate a string.

    Args:
        string: String to truncate
        length: Maximum string length before it gets truncated
            Default: 50
        suffix: String added to the end to indicate the data has been truncated
            Default: '...'

    Returns:
        <string> if len(string) < length else <string> truncated using
        <suffix> to indicate more data exists

    Example:
        >>> truncate('foo')
        'foo'
        >>> truncate('foo' * 20)
        'foofoofoofoofoofoofoofoofoofoofoofoofoofoofoofo...'
        >>>
        >>> truncate('foo' * 20, length = 30, suffix = '(tbc.)')
        'foofoofoofoofoofoofoofoo(tbc.)'
        >>>
    '''

    if len(string) < length:
        return string
    else:
        return string[:length - len(suffix)] + suffix
