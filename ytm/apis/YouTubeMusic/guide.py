from . import containers

__all__ = __name__.split('.')[-1:]

def guide(self):
    data = self.base.guide()

    container = containers.Guide \
    (
        api = self,
        data = data,
    )

    return container
