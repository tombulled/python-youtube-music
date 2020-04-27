def iso_time(duration: str) -> int:
    return sum \
    (
        60 ** index * int(item)
        for index, item in enumerate(duration.strip().split(':')[::-1])
    )
