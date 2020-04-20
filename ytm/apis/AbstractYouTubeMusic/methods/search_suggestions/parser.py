from ... import utils
from ... import decorators

__parser__ = __name__.split('.')[-1]
__method__ = __name__.split('.')[-2]
__all__ = (__parser__,)

@decorators.catch(__method__)
def parse(data):
    assert data
    
    contents = utils.get_nested \
    (
        data,
        'contents',
        0,
        'searchSuggestionsSectionRenderer',
        'contents',
        default = (),
    )

    assert contents

    suggestions = []

    for item in contents:
        item_runs = utils.get_nested \
        (
            item,
            'searchSuggestionRenderer',
            'suggestion',
            'runs',
            default = (),
        )

        if not item_runs:
            continue

        item_suggestion = ''

        for item_run in item_runs:
            item_run_text = utils.get_nested \
            (
                item_run,
                'text',
            )

            if item_run_text:
                item_suggestion += item_run_text

        if item_suggestion:
            suggestions.append(item_suggestion)

    return suggestions
