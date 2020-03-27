from . import containers
from  ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def watch(self, song_id, playlist_id=None):
    data = self.base.next \
    (
        video_id = song_id,
        playlist_id = playlist_id,
        # params = ytm_constants.PARAMS_WATCH,
        # player_params = ytm_constants.PARAMS_PLAYER_WATCH,
    )

    container = containers.Watch \
    (
        api = self,
        data = data,
    )

    return container
