__all__ = __name__.split('.')[-1:]

def search_suggestions(self):
    return self.api.search_suggestions(self.data)
