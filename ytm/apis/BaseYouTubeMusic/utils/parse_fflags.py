'''
Module containing the utility function: parse_fflags
'''

from .is_float import is_float

def parse_fflags(fflags: dict) -> dict:
    '''
    Parse fflags.

    Converts JavaScript values to Python values.
        E.g. 'true' -> True

    Args:
        fflags: Fflags to parse

    Returns:
        Parsed fflags

    Example:
        >>> fflags = \
        {
        	'html5_encrypted_vp9_firefox': 'true',
        	'html5_stop_video_in_cancel_playback': 'true',
        }
        >>>
        >>> parse_fflags(fflags)
        {'html5_encrypted_vp9_firefox': True, 'html5_stop_video_in_cancel_playback': True}
        >>>
    '''

    js_types = \
    {
        'true':  True,
        'false': False,
        'null':  None,
    }

    new_fflags = {}

    for fflag_key, fflag_val in fflags.items():
        if fflag_val in js_types:
            fflag_val = js_types[fflag_val]
        elif fflag_val.isdigit():
            fflag_val = int(fflag_val)
        elif is_float(fflag_val):
            fflag_val = float(fflag_val)

        new_fflags[fflag_key] = fflag_val

    return new_fflags
