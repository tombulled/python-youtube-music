'''
Module containing the utility function: rstrip
'''

def rstrip(string: str, sub_string: str) -> str:
    '''
    Right strip sub_string from string.

    Strips a phrase instead of a set of characters

    Args:
        string: Source string to strip from
        sub_string: Sub string to strip from string

    Returns:
        string right-stripped of sub_string

    Example:
        >>> rstrip('someData', 'Data')
        'some'
        >>>
    '''

    return string[:-len(sub_string) if string.endswith(sub_string) else -1]
