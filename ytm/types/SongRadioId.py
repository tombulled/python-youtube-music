from .SongId import SongId

class SongRadioId(SongId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMVM' + value

        return value
