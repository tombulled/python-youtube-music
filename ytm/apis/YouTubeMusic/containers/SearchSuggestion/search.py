__all__ = __name__.split('.')[-1:]

def search(self):
    return self.api.search(self.data)
