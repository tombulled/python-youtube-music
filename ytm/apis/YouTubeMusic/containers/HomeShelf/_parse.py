from ..... import utils as ytm_utils
from ..... import constants as ytm_constants
from ... import containers

import copy

__all__ = __name__.split('.')[-1:]

def _parse(self):
    # Convert items to HomeShelfItems
    data = copy.deepcopy(self.raw_data)
    items = ytm_utils.get_nested(data, 'items', default=())
    item_objects = []

    object_map = \
    {
        'Video': containers.HomeShelfVideo,
        'Playlist': containers.HomeShelfPlaylist,
        'Album': containers.HomeShelfAlbum,
        'Artist': containers.HomeShelfArtist,
        # Can also be a 'Single'
    }

    for item in items:
        item_type = ytm_utils.get_nested(item, 'type')

        if item_type not in object_map:
            return # raise

        item_obj = object_map[item_type](self.api, item)

        item_objects.append(item_obj)

    data['items'] = item_objects

    return data
