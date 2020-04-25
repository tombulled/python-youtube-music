def lstrip(string, sub_string):
    return string[len(sub_string) if string.startswith(sub_string) else 0:]
