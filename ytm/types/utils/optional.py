def optional(*values, required=False, group=None):
    return '({prefix}(?:{values}){quantifier})'.format \
    (
        values     = '|'.join(values),
        quantifier = '{1}' if required else '?',
        prefix     = f'?P<{group}>' if group else '',
    )
