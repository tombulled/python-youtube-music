'''
'''

def pad_base64(data: str) -> bool:
    '''
    '''

    mod = len(data) % 4

    if mod:
        data += '=' * (4 - mod)

    return data
