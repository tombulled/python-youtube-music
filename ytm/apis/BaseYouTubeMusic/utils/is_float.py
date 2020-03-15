__all__ = __name__.split('.')[-1:]

def is_float(string: str) -> bool:
    return all(char.isdigit() or char == '.' for char in string) and string.count('.') == 1
