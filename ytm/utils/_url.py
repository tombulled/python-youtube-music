'''
Module containing the utility function: _url
'''

import urllib.parse

def _url(protocol: str, domain: str, *endpoints: str, params: dict = None) -> str:
    '''
    Create a URL.

    Formulates a string URL using the arguments provided.

    Args:
        protocol: Domain protocol
            Example: 'http' or 'https'
        domain: Domain name
            Example: 'google.com'
        *endpoints: URL endpoints
            Example: ['directory', 'file.ext']
        params: URL query string parameters
            Example: {'username': 'admin', 'password': 'Password1'}

    Returns:
        A URL

    Example:
        >>> _url('http', 'www.google.co.uk', 'search', params={'q': 'test'})
        'http://www.google.co.uk/search?q=test'
        >>>
    '''

    return '{protocol}://{domain}/{endpoint}{parameters}'.format \
    (
        protocol   = protocol,
        domain     = domain,
        endpoint   = '/'.join(map(str.strip, endpoints)) if endpoints else '',
        parameters = f'?{urllib.parse.urlencode(params)}' if params else '',
    )
