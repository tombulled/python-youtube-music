'''
'''

def lstrip(string: str, sub_string: str) -> str:
    '''
    '''

    return string[len(sub_string) if string.startswith(sub_string) else 0:]
