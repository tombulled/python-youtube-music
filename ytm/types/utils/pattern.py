def pattern(*segments: str) -> str:
    prefix = '^'
    suffix = '$'
    sep    = ''

    if segments and isinstance(segments[0], bytes):
        prefix = prefix.encode()
        suffix = suffix.encode()
        sep    = sep.encode()

    return prefix + sep.join(segments) + suffix
