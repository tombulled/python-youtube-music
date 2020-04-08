from . import parsers

__all__ = __name__.split('.')[-1:]

def guide(self):
    data = self.base.guide()

    parsed_data = parsers.guide(data)

    return parsed_data
