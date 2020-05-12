# python-youtube-music

Unofficial Python YouTube Music Web API Client - **Still under active development**

![YouTube Music](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Logo_of_YouTube_Music.svg/1280px-Logo_of_YouTube_Music.svg.png)

## Dependencies - Required
| Library                                     | Install              | Import          | Functionality            |
| ------------------------------------------- | -------------------- | --------------- | ------------------------ |
| [Requests](https://github.com/psf/requests) | pip install requests | import requests | Send HTTP/HTTPS requests |

## Dependencies - Optional
| Library                                                 | Install                | Import            | Functionality                |
| ------------------------------------------------------- | ---------------------- | ----------------- | ---------------------------- |
| [YoutubeDL](https://github.com/ytdl-org/youtube-dl)     | pip install youtube-dl | import youtube_dl | Download YouTube videos      |
| [Mutagen](https://github.com/quodlibet/mutagen)         | pip install mutagen    | import mutagen    | Read and write audio metadata|
| [Pillow (PIL)](https://github.com/python-pillow/Pillow) | pip install Pillow     | import PIL        | Python imaging library       |

## Installation - From PyPi
In a terminal execute the command:
```
pip install ytm
```

## Installation - From Source
Clone/download this repository and in a terminal run setup.py:
```
cd python-youtube-music && python setup.py install
```

<!--
## Installation

### From Source
Clone this repository and run setup.py:
```
cd python-youtube-music && python setup.py install
```

## Getting Started
Initialise a YouTubeMusic instance
```python
>>> import ytm
>>>
>>> api = ytm.YouTubeMusic()
>>> api
<YouTubeMusic()>
>>>
```

## Types
Creating types
```python
>>> from ytm import types
>>>
>>> # Today's Biggest Hits
>>> playlist_id = 'RDCLAK5uy_mkLtojKLOUUGwnu3ZnN5AaODijlieB-aQ'
>>>
>>> # Create type object
>>> playlist_id = types.PlaylistId(playlist_id)
>>>
>>> # Check specific type
>>> types.utils.isinstance(playlist_id, types.PlaylistPlaylistId)
True
>>>
>>> # Convert type
>>> playlist_id = types.PlaylistPlaylistId(playlist_id)
>>> playlist_id
<PlaylistPlaylistId('RDCLAK5uy_mkLtojKLOUUGwnu3ZnN5AaODijlieB-aQ')>
>>>
```

Creating types with an invalid value

```python
>>> from ytm import types
>>>
>>> playlist_id = types.PlaylistId('invalid')
TypeError: Invalid PlaylistId: 'invalid'
>>> 
```

Enforcing types for a function
```python
>>> from ytm import types
>>> from ytm import decorators
>>> 
>>> @decorators.typecheck
def my_func(song_id: types.SongId):
	print('song_id:', song_id)
>>>	
>>> my_func
<function my_func at 0x0000028B4319BD30>
>>> 
>>> song_id_str = 'L-NbInXED-o'
>>> song_id_type = types.SongId(song_id_str)
>>> 
>>> # Passing a valid string
>>> my_func(song_id_str)
song_id: L-NbInXED-o
>>> 
>>> # Passing a correct type
>>> my_func(song_id_type)
song_id: L-NbInXED-o
>>> 
>>> # Passing an invalid string
>>> my_func('not a valid SongId')
TypeError: my_func() expected parameter 'song_id' to be of type 'SongId' not 'str'
>>> 
```

## Utilities
Utility functions
```python
>>> from ytm import utils
>>> 
>>> # Create a YouTube Music URL
>>> utils.url('watch', {'v': '0d2llFWvFSM', 'list': 'RDAOazj3phJrB390ewqF8AaC-w'})
'https://music.youtube.com/watch?v=0d2llFWvFSM&list=RDAOazj3phJrB390ewqF8AaC-w'
>>> 
>>> # Create a YouTube URL
>>> utils.url_yt('playlist', {'list': 'RDCLAK5uy_lZjWT2hQC7Gb_1_Las16IryBLhnCMgdIo'})
'https://www.youtube.com/playlist?list=RDCLAK5uy_lZjWT2hQC7Gb_1_Las16IryBLhnCMgdIo'
>>>
>>> # Filter a dictionary
>>> utils.filter({'name': 'Gotye', 'id': None}, lambda key, val: val is not None)
{'name': 'Gotye'}
>>> 
>>> # Massively nested iterable
>>> iterable = {'data': {'results': [{'value': 'Wozniak'}]}}
>>>
>>> # Get a specific value from an iterable
>>> utils.get(iterable, 'data', 'results', 0, 'value')
'Wozniak'
>>> 
```
-->
