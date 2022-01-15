'''
Module containing the Id type: ArtistRadioId
'''

from .. import base
from .. import constants

class ArtistRadioId(base.Id):
    '''
    Id class: ArtistRadioId

    Example:
        >>> id = ArtistRadioId('RDEMHSpo_Uv9STIRtF73zMywLg')
        >>>
        >>> id
        <ArtistRadioId('RDEMHSpo_Uv9STIRtF73zMywLg')>
        >>>
        >>> str(id)
        'RDEMHSpo_Uv9STIRtF73zMywLg'
        >>>
    '''

    _pattern: str = '^(?P<prefix>{prefixes})(?P<data>[{chars}]{{{entropy_length}}})$'.format \
    (
        prefixes       = '|'.join \
        (
            (
                constants.PREFIX_ARTIST_RADIO_ID,
                constants.PREFIX_ARTIST_SHUFFLE_ID,
            ),
        ),
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ARTIST_ID,
    )

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        Clean the extracted data value.

        Append the artist radio prefix to the value.

        Args:
            cls: This class
            value: The extracted data value to clean

        Returns:
            Cleaned value

        Example:
            >>> ArtistRadioId._clean('HSpo_Uv9STIRtF73zMywLg')
            'RDEMHSpo_Uv9STIRtF73zMywLg'
            >>>
        '''

        return constants.PREFIX_ARTIST_RADIO_ID + value
