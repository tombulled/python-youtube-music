from .. import constants

def entropy(length: int = None, chars: str = None, name: str = None, repeat: str = None) -> str:
    # repeat: '+' or '*' etc.
    if not chars:
        chard = constants.CHARS_ID
    elif len(chars) > 1:
        chars = f'[{chars}]'

    return '({prefix}(?:{chars}{{{length}}}){repeat})'.format \
    (
        prefix = f'?P<{name}>' if name else '?:',
        chars  = chars,
        length = length or 1,
        repeat = repeat or '',
    )
