from . import containers

__all__ = __name__.split('.')[-1:]

def home(self):
    data = self.base.browse_home()

    container = containers.Home \
    (
        api = self,
        data = data,
    )

    return container
