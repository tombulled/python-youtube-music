'''
'''

import urllib.parse

def _url(protocol, domain, endpoints, params: dict = None) -> str:
    '''
    '''

    return '{protocol}://{domain}/{endpoint}{parameters}'.format \
    (
        protocol = protocol,
        domain   = domain,
        endpoint = '/'.join(map(str.strip, endpoints)) if endpoints else '',
        parameters = f'?{urllib.parse.urlencode(params)}' if params else '',
    )
