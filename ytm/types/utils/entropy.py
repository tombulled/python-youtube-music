'''
'''

from .. import constants

def entropy \
        (
            length: int = None,
            chars:  str = None,
            name:   str = None,
            repeat: str = None,
        ) -> str:
    '''
    TmpNote: repeat: '+' or '*' etc.
    '''

    if not chars:
        chars = constants.CHARS_ID

    if len(chars) > 1:
        chars = f'[{chars}]'

    return '({prefix}(?:{chars}{{{length}}}){repeat})'.format \
    (
        prefix = f'?P<{name}>' if name else '?:',
        chars  = chars,
        length = length or 1,
        repeat = repeat or '',
    )
