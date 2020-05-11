'''
Module containing the cleanser: ascii_time
'''

def ascii_time(duration: str) -> int:
    '''
    Convert an ASCII representation of time into duration in seconds.

    The ASCII representation follows the following format:
        {} hours, {} minutes, {} seconds
    Each group is optional and treated case-insensitively.

    Args:
        duration: ASCII duration string
            Example: '2 hours, 36 seconds'

    Returns:
        Duration in seconds

    Example:
        >>> time = '11 hours, 22 minutes, 33 seconds'
        >>>
        >>> ascii_time(time)
        40953
        >>>
    '''

    return sum \
    (
        60 ** scalar * value
        for value_str, slot_name in map \
        (
            lambda segment: segment.strip().split(' '),
            duration.lower().split(','),
        )
        for value, scalar in \
        (
            (
                int(value_str),
                (
                    'seconds',
                    'minutes',
                    'hours',
                ).index(slot_name)
            ),
        )
    )
