'''
Module containing the method: browse_artist
'''

def browse_artist(self: object, browse_id: str) -> dict:
    '''
    Return browse data for: Artist.

    See help for the 'browse' method for more information

    Args:
        self: Class instance
        browse_id: Artist browse id
            Example: 'UC8Yu1_yfN5qPh601Y4btsYw'

    Returns:
        Artist browse data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_artist('UC8Yu1_yfN5qPh601Y4btsYw')
        >>>
        >>> data['header']['musicImmersiveHeaderRenderer']['title']
        {'runs': [{'text': 'Arctic Monkeys'}]}
        >>>
    '''

    return self.browse \
    (
        browse_id = browse_id,
    )
