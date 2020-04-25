from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_suggestions(data: dict):
    assert data, 'No data to parse'

    contents = utils.get \
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
        item_runs = utils.get \
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
            item_run_text = utils.get \
            (
                item_run,
                'text',
            )

            if item_run_text:
                item_suggestion += item_run_text

        if item_suggestion:
            suggestions.append(item_suggestion)

    return suggestions
