'''
'''

from ..utils import _import

_import(locals())

USER_AGENTS = \
(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
)

# Headers
HEADER_VISITOR_ID = 'CgtqQXdSZDY3c29hSSiPsr_uBQ%3D%3D'
HEADER_DO_NOT_TRACK = '1'
HEADER_TRAILERS = 'Trailers'

# Domains
DOMAIN_YOUTUBE_MUSIC = 'music.youtube.com'
DOMAIN_YOUTUBE       = 'www.youtube.com'

# Protocols
PROTOCOL_HTTPS = 'https'
PROTOCOL_HTTP  = 'http'

# Domain Protocols
PROTOCOL_YOUTUBE       = PROTOCOL_HTTPS
PROTOCOL_YOUTUBE_MUSIC = PROTOCOL_HTTPS

VERSION_YTM_API = 1

# YoutubeMusic API Endpoints
ENDPOINT_YTM_API = f'youtubei/v{VERSION_YTM_API}/'
