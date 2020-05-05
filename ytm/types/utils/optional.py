'''
'''

def optional \
        (
            *values:  str,
            required: bool = False,
            group:    str  = None,
        ) -> str:
    '''
    '''

    return '({prefix}(?:{values}){quantifier})'.format \
    (
        values     = '|'.join(values),
        quantifier = '{1}' if required else '?',
        prefix     = f'?P<{group}>' if group else '?:',
    )
