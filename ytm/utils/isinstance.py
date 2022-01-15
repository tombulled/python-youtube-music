'''
Module containing the utility function: isinstance
'''

import builtins

def isinstance(object: object, class_: type) -> bool:
    '''
    Return whether an object is an instance of a class or of a subclass thereof.

    Modified to work with custom types, specifically with a _validate method

    Args:
        object: Object to check whether it's an instance of class_
            Example: 'foo' or types.SongId('5HzWqJ8HZ5g')
        class_: Class to check whether object is an instance of it
            Example: str or types.SongId

    Returns:
        Whether object is an instance of class_

    Example:
        Normal type:
            >>> isinstance('foo', str)
            True
            >>>
        Custom type:
            >>> isinstance('invalid_song_id', types.SongId)
            False
            >>>
    '''

    return (builtins.isinstance(class_, type) and builtins.isinstance(object, class_)) \
        or getattr(class_, '_isinstance', lambda object: False)(object)
