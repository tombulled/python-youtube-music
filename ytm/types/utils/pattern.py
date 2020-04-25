def pattern(*segments: str) -> str:
    return '^' + ''.join(segments) + '$'
