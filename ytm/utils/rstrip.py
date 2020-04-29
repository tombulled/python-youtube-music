'''
'''

def rstrip(string: str, sub_string: str) -> str:
    return string[:-len(sub_string) if string.endswith(sub_string) else -1]
