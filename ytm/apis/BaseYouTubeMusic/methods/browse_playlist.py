'''
Module containing the method: browse_playlist
'''

def browse_playlist(self: object, browse_id: str) -> dict:
    '''
    Return browse data for: Playlist.

    See help for the 'browse' method for more information

    Args:
        self: Class instance
        browse_id: Playlist browse id
            Example: 'VLPL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM'

    Returns:
        Playlist browse data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_playlist('VLPL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM')
        >>>
        >>> data['header']['musicDetailHeaderRenderer']['title']
        {'runs': [{'text': 'Top 100 Music Videos Global'}]}
        >>>
    '''

    return self.browse \
    (
        browse_id = browse_id,
    )
