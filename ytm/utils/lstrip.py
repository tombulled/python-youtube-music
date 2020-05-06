'''
Module containing the utility function: lstrip
'''

def lstrip(string: str, sub_string: str, count: int = None) -> str:
    """
    Left strip <count> <sub_string>'s from <string>.

    Strips a phrase instead of a set of characters.

    Args:
        string: Source string to strip from
        sub_string: Sub string to strip from string
        count: Maximum number of sub strings to strip
            Default: 1

    Returns:
        <string> left-stripped of <sub_string> <count> times

    Examples:
        >>> lstrip('someData', 'some')
        'Data'
        >>> lstrip('somesomeData', 'some', 2)
        'Data'
    """

    if not isinstance(count, int) or count <= 0:
        count = 1

    for _ in range(count):
        if string.startswith(sub_string):
            string = string[len(sub_string):]

    return string
