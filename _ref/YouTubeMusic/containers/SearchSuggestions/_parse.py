from ..... import utils as ytm_utils
from ... import containers
# from ..SearchSuggestion import SearchSuggestion

__all__ = __name__.split('.')[-1:]

def _parse(self):
    contents = ytm_utils.get_nested \
    (
        self.raw_data,
        'contents',
        0,
        'searchSuggestionsSectionRenderer',
        'contents',
        default = [],
    )

    suggestions = []

    for item in contents:
        suggestion = ''.join \
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

        # suggestion_obj = SearchSuggestion(suggestion)
        # print('Creating search suggestion:', self.api, repr(suggestion))

        suggestion_obj = containers.SearchSuggestion(suggestion) # self.api, suggestion)
        suggestion_obj.api = self.api
        suggestion_obj.raw_data = suggestion
        suggestion_obj.data = suggestion

        suggestions.append(suggestion_obj)

    return suggestions
