def rstrip(string, sub_string):
    return string[:-len(sub_string) if string.endswith(sub_string) else -1]
