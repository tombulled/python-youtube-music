from . import base
from . import utils

class ArtistRadioId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.optional \
            (
                'RDEM',
                'RDAO',
            ),
            utils.entropy(22),
        ),
    )

    @classmethod
    def _clean(cls, value: str):
        value = utils.lstrip(value, 'RDEM')
        value = utils.lstrip(value, 'RDAO')

        value = 'RDEM' + value

        return value
