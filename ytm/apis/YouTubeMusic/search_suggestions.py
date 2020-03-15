from ... import utils as ytm_utils

def search_suggestions(self, query):
    data = self.base.search_suggestions \
    (
        query = query
    )

    suggestions = \
    [
        ''.join \
        (
            run['text']
            for run in ytm_utils.get_nested \
            (
                item,
                'searchSuggestionRenderer',
                'suggestion',
                'runs',
            )
        )
        for item in ytm_utils.get_nested \
        (
            data,
            'contents',
            0,
            'searchSuggestionsSectionRenderer',
            'contents',
            default = [],
        )
    ]

    return suggestions
