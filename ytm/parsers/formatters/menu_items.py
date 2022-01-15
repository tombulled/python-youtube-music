'''
'''

from ... import utils

def menu_items(data):
    '''
    '''
    
    menu_data = {}

    for menu_item in data:
        menu_item = utils.first(menu_item)

        for key, val in menu_item.copy().items():
            if not key.startswith('default'):
                continue

            new_key = key.replace('default', '')
            new_key = new_key[0].lower() + new_key[1:]

            menu_item[new_key] = menu_item.pop(key)

        menu_text = utils.get \
        (
            menu_item,
            'text',
            'runs',
            0,
            'text',
        )
        menu_icon = utils.get \
        (
            menu_item,
            'icon',
            'iconType',
        )
        menu_endpoint = utils.get \
        (
            menu_item,
            'navigationEndpoint',
        )

        if not menu_endpoint:
            continue

        menu_identifier = menu_text[0].lower() + menu_text.title()[1:].replace(' ', '') \
            if menu_text else None

        menu_item_data = \
        {
            'text':     menu_text,
            'icon':     menu_icon,
            'endpoint': menu_endpoint,
        }

        menu_data[menu_identifier] = menu_item_data

    return menu_data
