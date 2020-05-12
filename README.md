# python-youtube-music

Python YouTube Music Web API Client - **Still under active development**

![YouTube Music](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Logo_of_YouTube_Music.svg/1280px-Logo_of_YouTube_Music.svg.png)

## Contents:
* [Dependencies - Required](#)
* [Dependencies - Optional](#)
* [Installation - From PyPi](#)
* [Installation - From Source](#)
* [Getting Started](#)
* [Method - Album](#)

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
python setup.py install
```

## Getting Started
Create an API instance
```python
>>> import ytm
>>> 
>>> api = ytm.YouTubeMusic()
>>> api
<YouTubeMusic()>
>>> 
````

View available methods

```python
>>> from pprint import pprint
>>> 
>>> pprint(list(api._methods))
['_search_filter',
 'album',
 'artist',
 'artist_albums',
 'artist_singles',
 'guide',
 'home',
 'hotlist',
 'playlist',
 'search',
 'search_albums',
 'search_artists',
 'search_playlists',
 'search_songs',
 'search_suggestions',
 'search_videos',
 'song',
 'watch',
 'watch_radio',
 'watch_shuffle']
>>> 
```

## Method - Album

Retrieve information about an album.

<details>
<summary>View Example</summary>
<p>
	
```python
>>> album = api.album('MPREb_ctJ5HEJw8pg') # Band Of Horses - Everything All The Time
>>> 
>>> list(album)
['name', 'id', 'total_tracks', 'radio', 'shuffle', 'explicit', 'duration', 'date', 'type', 'thumbnail', 'description', 'artists', 'tracks', 'variants']
>>> 
>>> album['name']
'Everything All The Time'
>>> album['total_tracks']
10
>>> album['explicit']
False
>>> album['duration']
2169367
>>> album['date']
{'year': 2006, 'month': 3, 'day': 21}
```
</p>
</details>

## Method - Artist
```python
>>> # TODO
```

## Method - Artist Albums
```python
>>> # TODO
```

## Method - Artist Singles
```python
>>> # TODO
```

## Method - Guide
```python
>>> guide = api.guide()
>>> 
>>> guide
{'Home': 'FEmusic_home', 'Hotlist': 'FEmusic_trending', 'Library': 'FEmusic_liked'}
>>> 
```

## Method - Home
```python
>>> home = api.home()
>>> 
>>> list(home)
['continuation', 'shelves']
>>> 
>>> for shelf in home['shelves']:
	print(shelf['name'])
	
Top charts
Relaxing to Country
>>>
>>> # Continue Data
>>> home2 = api.home(home['continuation'])
>>>
>>> for shelf in home2['shelves']:
	print(shelf['name'])

Office radio
Today's hits
Cool vibes
>>> 
```

## Method - Hotlist
```python
>>> hotlist = api.hotlist()
>>> 
>>> for song in hotlist:
	print(' & '.join(song['artist']['names']), '-', song['name'])

Ariana Grande & Justin Bieber - Stuck with U
Migos - Racks 2 Skinny
ManBetterKnow - Nang
Dua Lipa - Break My Heart
Little Mix - Break Up Song (Acoustic Version)
Grm Daily - S1mba - Rover (Remix) (ft. Poundz, ZieZie & Ivorian Doll) [Music Video] | GRM Daily
Lil Durk - Doin Too Much
Black Pepper - Black Pepper - Dublue
Hayley Williams - Dead Horse
slowthai - slowthai - ENEMY
GRM Daily - Offica - Face Reveal [Music Video] | GRM Daily
Example - Example - 'Erin' (Official Video) (OUT NOW)
Mumford & Sons - Forever
Headie One - HEADIE ONE - ROSE GOLD
Jaykae - Jaykae - Novocaine [feat. Remtrex] (Official Video)
NAV - No Debate
The 1975 - Me & You Together Song
SBK - SBK - Numbers (Official Video)
Sean Paul - Back It up Deh
Baauer - AETHER
>>> 
>>> 
```

## Method - Playlist
```python
>>> # TODO
```

## Method - Search
```python
>>> results = api.search('alt-j')
>>> 
>>> list(results)
['albums', 'playlists', 'videos', 'artists', 'songs', 'top_result']
>>> 
>>> results['top_result']
'artist'
>>> 
>>> results['artists'][0]['name']
'alt-J'
>>> 
>>> results['albums'][0]['name']
'An Awesome Wave'
>>> 
```

## Method - Search Albums
```python
>>> albums = api.search_albums('nevermind')
>>> 
>>> for album in albums['items'][:5]: # First 5 Albums
	print(album['artist']['name'], '-', album['name'])

Nirvana - Nevermind
Alexander Jean - Nevermind
Sex Pistols - Never Mind The Bollocks, Here's The Sex Pistols (40th Anniversary Deluxe Edition)
Poyo Spirit - Nevermind
Distruction Boyz, Zhao - Nevermind (Radio Edit)
>>> 
>>> # Continue Data
>>> albums2 = api.search_albums(continuation = albums['continuation'])
>>> 
>>> for album in albums2['items'][:5]: # First 5 Albums
	print(album['artist']['name'], '-', album['name'])

Soriya - Nevermind
Wisp X - Nevermind
P_frmdatribe - Nevermind
Renel - Nevermind
Jacob Lee - Nevermind
>>> 
```

## Method - Search Artists
```python
>>> artists = api.search_artists('john')
>>> 
>>> for artist in artists['items'][:5]: # First 5 Artists
	print(artist['name'])

John Legend
John Mayer
John Newman
Elton John
John Lennon
>>> 
>>> # Continue Data
>>> artists2 = api.search_artists(continuation = artists['continuation'])
>>> 
>>> for artist in artists2['items'][:5]: # First 5 Artists
	print(artist['name'])

	
John Mellencamp
John Carpenter
John Williams
John Coltrane
John Barry
>>> 
```

## Method - Search Playlists
```python
>>> playlists = api.search_playlists('indie')
>>> 
>>> for playlist in playlists['items'][:5]: # First 5 Playlists
	print(playlist['name'])

Coffee Shop Indie
Upbeat Indie Pop
Indie Folk Favorites
Indie Rock Chasers
Take It Easy Indie
>>> 
>>> # Continue Data
>>> playlists2 = api.search_playlists(continuation = playlists['continuation'])
>>> 
>>> for playlist in playlists2['items'][:5]: # First 5 Playlists
	print(playlist['name'])
	
A Decade of Easy Indie
Indie Disco Overload
Sunshine Indie
Pop & Indie Easy Listening
00s Indie Guitar Anthems
>>> 
```

## Method - Search Songs
```python
>>> songs = api.search_songs('cry')
>>> 
>>> for song in songs['items'][:5]: # First 5 Songs
	print(song['artists'][0]['name'], '-', song['name'])

Rihanna - Cry
KAZKA - CRY (English Version)
James Blunt - Cry
Carly Rae Jepsen - Cry
System F - Cry (Original Extended)
>>> 
>>> # Continue Data
>>> songs2 = api.search_songs(continuation = songs['continuation'])
>>> 
>>> for song in songs2['items'][:5]: # First 5 Songs
	print(song['artists'][0]['name'], '-', song['name'])
	
Marilyn Manson - Cry Little Sister
Jorja Smith - Don't Watch Me Cry
Oasis - Stop Crying Your Heart Out
Volbeat - I'm So Lonesome I Could Cry
Coldplay - Cry Cry Cry
>>> 
```

## Method - Search Videos
```python
>>> videos = api.search_videos('time')
>>> 
>>> for video in videos['items'][:5]: # First 5 Videos
	print(video['artist']['name'], '-', video['name'])

Lizzy Capri - Lizzy Capri - TIME (Official Lyric Video)
NF - Time
Pink Floyd Remasted Songs - Pink Floyd - Time (2011 Remastered)
Chase & Status - Time
Lil Baby - Time
>>> 
>>> # Continue Data
>>> videos2 = api.search_videos(continuation = videos['continuation'])
>>> 
>>> for video in videos2['items'][:5]: # First 5 Videos
	print(video['artist']['name'], '-', video['name'])

Anjunadeep - Simon Doty feat. Forrest - This Time
Alesso - TIME
Imagine Dragons - It's Time
Culture Club - Time (Clock of the Heart)
Freddie Mercury - Time Waits For No One
>>> 
```

## Method - Search Suggestions
```python
>>> suggestions = api.search_suggestions('foo fight')
>>> 
>>> from pprint import pprint
>>> 
>>> pprint(suggestions)
['foo fighters',
 'foo fighters everlong',
 'foo fighters times like these',
 'foo fighters learn to fly',
 'foo fighters best of you',
 'foo fighters live',
 'foo fighters pretender']
>>> 
```

## Method - Song
```python
>>> song = api.song('pPt_FZ9m2bM')
>>> 
>>> list(song)
['id', 'name', 'views', 'rating', 'duration', 'explicit', 'description', 'thumbnail', 'owner', 'artist', 'date']
>>> 
>>> song['name']
'The Key to Life on Earth'
>>> song['owner']['name']
'Declan McKenna'
>>> song['views']
53130
>>> song['rating']
4.9008608
>>> song['duration']
247
>>> song['explicit']
False
>>> song['date']
{'year': 2020, 'month': 4, 'day': 14}
>>> 
```

## Method - Watch
```python
>>> # TODO
```

## Method - Watch Radio
```python
>>> # TODO
```

## Method - Watch Shuffle
```python
>>> # TODO
```

<!-- ################################################################################################## -->


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
