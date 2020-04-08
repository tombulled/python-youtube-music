from . import parsers

__all__ = __name__.split('.')[-1:]

def home(self, continuation=None):
    if continuation:
        data = self.base.browse \
        (
            continuation = continuation,
        )
    else:
        data = self.base.browse_home()

    parsed_data = parsers.browse_home(data)

    return parsed_data
