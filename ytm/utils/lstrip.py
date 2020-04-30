'''
Module containing the utility function: lstrip
'''

def lstrip(string: str, sub_string: str) -> str:
    '''
    Left strip sub_string from string.

    Strips a phrase instead of a set of characters

    Args:
        string: Source string to strip from
        sub_string: Sub string to strip from string

    Returns:
        string left-stripped of sub_string

    Example:
        >>> lstrip('someData', 'some')
        'Data'
        >>>
    '''

    return string[len(sub_string) if string.startswith(sub_string) else 0:]
