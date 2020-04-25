from .SongId import SongId

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class SongRadioId(SongId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMVM' + value

        return value
