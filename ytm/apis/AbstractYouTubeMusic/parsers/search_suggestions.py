from .... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def search_suggestions(data):
    contents = ytm_utils.get_nested \
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
        suggestion = ''.join \
        (
            ytm_utils.get_nested(run, 'text', default = '')
            for run in ytm_utils.get_nested \
            (
                item,
                'searchSuggestionRenderer',
                'suggestion',
                'runs',
            )
        )

        if suggestion:
            suggestions.append(suggestion)

    return suggestions
