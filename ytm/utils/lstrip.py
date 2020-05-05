'''
Module containing the utility function: lstrip
'''

def lstrip(string: str, sub_string: str, strip_count: int = 1) -> str:
    """
    Left strip strip_count sub_string's from <string>.

    Strips a phrase instead of a set of characters.

    Args:
        string: Source string to strip from.
        sub_string: Sub string to strip from string.
        strip_count: Maximum number of substrings to strip. Defaults to one.

    Returns:
        string left-stripped of sub_string
    
    Raises:
        ValueError: If strip_count is less than one.
        
    Examples:
        >>> lstrip('someData', 'some', 1)
        'Data'
        >>> lstrip('somesomesomesom', 'some', 2)
        'somesom'
    """
    if strip_count <= 0:
        raise ValueError
        
    strip_counter = 0
    
    while string.startswith(substring):
        if strip_counter > strip_count:
            string = string[len(subs_tring):]
            strip_counter += 1
        else:
            break
     
    return string
