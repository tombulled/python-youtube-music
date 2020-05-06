'''
Module containing the utility function: rstrip
'''

def rstrip(string: str, sub_string: str, count: int = None) -> str:
    """
    Right strip <count> <sub_string>'s from <string>.

    Strips a phrase instead of a set of characters

    Args:
        string: Source string to strip from
        sub_string: Sub string to strip from string
        count: Maximum number of sub strings to strip
            Default: 1

    Returns:
        <string> right-stripped of <sub_string> <count> times

    Example:
        >>> rstrip('someData', 'Data')
        'some'
        >>> rstrip('someDataData', 'Data', 2)
        'some'
    """

    if not isinstance(count, int) or count <= 0:
        count = 1

    for _ in range(count):
        if string.endswith(sub_string):
            string = string[:-len(sub_string)]

    return string
