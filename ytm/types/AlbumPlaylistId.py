from . import base
from . import utils
from . import constants

prefixes = \
(
    constants.PREFIX_ALBUM_RADIO_ID,
)

class AlbumPlaylistId(base.BaseType):
    # _patterns = \
    # (
    #     # utils.pattern \
    #     # (
    #     #     utils.optional(constants.PREFIX_ALBUM_RADIO_ID),
    #     #     constants.PREFIX_ALBUM_PLAYLIST_ID,
    #     #     utils.entropy(constants.LEN_ENTROPY_ALBUM_PLAYLIST_ID),
    #     # ),
    #     ''.join \
    #     (
    #         (
    #             '^',
    #             '(',
    #                 '?P<prefix>',
    #                 '|'.join(prefixes),
    #             ')',
    #             '(',
    #                 '?P<data>',
    #                 constants.PREFIX_ALBUM_PLAYLIST_ID,
    #                 '[',
    #                     constants.CHARS_ID,
    #                 ']',
    #                 '{',
    #                     str(constants.LEN_ENTROPY_ALBUM_PLAYLIST_ID),
    #                 '}',
    #             ')',
    #             '$',
    #         ),
    #     ),
    # )

    _pattern = \
    (
        '^'
        '(?P<prefix>'
            f'{"|".join(prefixes)}'
        ')?'
        '(?P<data>'
            f'{constants.PREFIX_ALBUM_PLAYLIST_ID}'
            f'[{constants.CHARS_ID}]'
            f'{{{constants.LEN_ENTROPY_ALBUM_PLAYLIST_ID}}}'
        ')'
        '$'
    )

    @classmethod
    def _clean(cls: type, value: str) -> str:
        return utils.lstrip(value, constants.PREFIX_ALBUM_RADIO_ID)
