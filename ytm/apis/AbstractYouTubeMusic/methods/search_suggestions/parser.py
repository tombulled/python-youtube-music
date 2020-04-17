# from ..... import utils as utils
from ... import utils

__all__ = __name__.split('.')[-1:]

def parse(data):
    contents = utils.get_nested \
    (
        data,
        'contents',
        0,
        'searchSuggestionsSectionRenderer',
        'contents',
        default = (),
    )

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
