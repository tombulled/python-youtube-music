from . import parsers

__all__ = __name__.split('.')[-1:]

def hotlist(self):
    data = self.base.browse_hotlist()

    parsed_data = parsers.browse_hotlist(data)

    return parsed_data
