'''
Module containing the Api class: BaseYouTubeMusic
'''

import requests

from . import utils
from . import methods

class BaseYouTubeMusic(object):
    '''
    Base YouTube Music class.

    Lowest level interactions with YouTube Music are achieved using this class

    Attributes:
        _session: Requests session for sending requests
        _params: URL GET request parameters
        _payload: YouTube Music base payload
    '''

    _session: requests.Session = None
    _params:  dict             = {}
    _payload: dict             = {}

    def __init__(self: object) -> None:
        '''
        Initialise class.

        Args:
            self: Class instance

        Returns:
            None

        Example:
            >>> api = BaseYouTubeMusic()
        '''

        for method_name in methods.__all__:
            method = getattr(methods, method_name)

            setattr(self.__class__, method_name, method)

        self._session = requests.Session()

        self._session.headers.update \
        (
            {
                'User-Agent': utils.random_user_agent(),
                'Referer'   : self._url(),
            }
        )

        self._update()

    def __repr__(self: object) -> str:
        '''
        Return a string representation of the object.

        Returns a string in the format <{class_name}()>

        Args:
            self: Class instance

        Returns:
            String representation of the object

        Example:
            >>> api = BaseYouTubeMusic()
            >>>
            >>> api
            <BaseYouTubeMusic()>
            >>>
        '''

        return '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

    def _update(self: object) -> None:
        '''
        Update the API's core values.

        Args:
            self: Class instance

        Returns:
            None

        Example:
            >>> api = BaseYouTubeMusic()
            >>>
            >>> api._update()
            >>>
        '''

        page = self.page_home()

        self._payload = \
        {
            'context': \
            {
                'client': \
                {
                    'gl': 'US',
                    'hl': 'en',
                },
            },
        }

        self._session.headers.update \
        (
            {
                'X-YouTube-Time-Zone':  'Europe/London',
                'X-YouTube-Utc-Offset': '60',
            }
        )

        mappings = \
        (
            {
                'container': self._session.headers,
                'mapping': \
                {
                    'X-Goog-Visitor-Id':        'VISITOR_DATA',
                    'X-YouTube-Client-Name':    'INNERTUBE_CONTEXT_CLIENT_NAME',
                    'X-YouTube-Client-Version': 'INNERTUBE_CONTEXT_CLIENT_VERSION',
                    'X-YouTube-Device':         'DEVICE',
                    'X-YouTube-Page-CL':        'PAGE_CL',
                    'X-YouTube-Page-Label':     'PAGE_BUILD_LABEL',
                },
            },
            {
                'container': self._params,
                'mapping': \
                {
                    'key': 'INNERTUBE_API_KEY',
                },
            },
            {
                'container': self._payload['context']['client'],
                'mapping': \
                {
                    'clientName':    'INNERTUBE_CLIENT_NAME',
                    'clientVersion': 'INNERTUBE_CLIENT_VERSION',
                    # The below regional information has been disabled as it may
                    # interfere with the API which relies on the response being English.
                    # 'gl':            'GL',
                    # 'hl':            'HL',
                },
            },
        )

        for mapping_entry in mappings:
            container = mapping_entry['container']
            mapping   = mapping_entry['mapping']

            for container_key, page_key in mapping.items():
                container_val = page.get(page_key)

                if container_val:
                    container[container_key] = str(container_val)
