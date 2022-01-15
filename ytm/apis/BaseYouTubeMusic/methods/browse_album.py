'''
Module containing the method: browse_album
'''

def browse_album(self: object, browse_id: str) -> dict:
    '''
    Return browse data for: Album.

    See help for the 'browse' method for more information

    Args:
        self: Class instance
        browse_id: Album browse id
            Example: 'MPREb_GFKho1A5P3G'

    Returns:
        Album browse data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_album('MPREb_GFKho1A5P3G')
        >>>
        >>> data.keys()
        dict_keys(['responseContext', 'contents', 'header', ...])
        >>>
    '''

    return self.browse \
    (
        browse_id = browse_id,
    )
