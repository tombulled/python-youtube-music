'''
Module containing the cleanser: iso_time
'''

def iso_time(duration: str) -> int:
    '''
    Convert an ISO duration string to duration in seconds

    An ISO duration string follows the format:
        h:m:s
    Where each group is optional (E.g. m:s is perfectly valid).

    Args:
        duration: ISO duration string
            Example: 11:22:33

    Returns:
        Duration in seconds

    Example:
        >>> time = '01:25:59'
        >>> 
        >>> iso_time(time)
        5159
        >>>
    '''

    return sum \
    (
        60 ** index * int(item)
        for index, item in enumerate(duration.strip().split(':')[::-1])
    )
