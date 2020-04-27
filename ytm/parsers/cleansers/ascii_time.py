def ascii_time(duration: str):
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
