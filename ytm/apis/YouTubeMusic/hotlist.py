from . import containers

__all__ = __name__.split('.')[-1:]

def hotlist(self):
    data = self.base.browse_hotlist()

    container = containers.Hotlist \
    (
        api = self,
        data = data,
    )

    return container
