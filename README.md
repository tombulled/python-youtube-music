# python-youtube-music

Python YouTube Music Web API Client - **Still under active development**

![YouTube Music](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Logo_of_YouTube_Music.svg/1280px-Logo_of_YouTube_Music.svg.png)

## Contents:
* [Dependencies - Required](#dependencies---required)
* [Dependencies - Optional](#dependencies---optional)
* [Installation - From PyPi](#installation---from-pypi)
* [Installation - From Source](#installation---from-source)
* [Getting Started](#getting-started)
* [Method - Album](#method---album)
* [Method - Artist](#method---artist)
* [Method - Artist Albums](#method---artist-albums)
* [Method - Artist Singles](#method---artist-singles)
* [Method - Guide](#method---guide)
* [Method - Home](#method---home)
* [Method - Hotlist](#method---hotlist)
* [Method - Playlist](#method---playlist)
* [Method - Search](#method---search)
* [Method - Search Albums](#method---search-albums)
* [Method - Search Artists](#method---search-artists)
* [Method - Search Playlists](#method---search-playlists)
* [Method - Search Songs](#method---search-songs)
* [Method - Search Videos](#method---search-videos)
* [Method - Search Suggestions](#method---search-suggestions)
* [Method - Song](#method---song)
* [Method - Watch](#method---watch)
* [Method - Watch Radio](#method---watch-radio)
* [Method - Watch Shuffle](#method---watch-shuffle)

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
```console
user@host:~$ pip install ytm # You may need to use: python3 -m pip install ytm
Successfully installed ytm
```

## Installation - From Source
Clone/download this repository and run setup.py:
```console
user@host:~$ python setup.py install # You may need to use: python3 setup.py install
Successfully installed ytm
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

Retrieve information about an artist.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

## Method - Artist Albums

Retrieve information about an artist's albums.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

## Method - Artist Singles

Retrieve information about an artist's singles.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

## Method - Guide

Retrieve information about available tabs.

<details>
<summary>View Example</summary>
<p>

```python
>>> guide = api.guide()
>>> 
>>> guide
{'Home': 'FEmusic_home', 'Hotlist': 'FEmusic_trending', 'Library': 'FEmusic_liked'}
>>> 
```

</p>
</details>

## Method - Home

Retrieve information about the home page

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Hotlist
Retrieve information about songs in the hotlist.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Playlist
Retrieve information about a playlist.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

## Method - Search

Retrieve information about a specific search.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Search Albums
Retrieve information about a albums related to a specific search query.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Search Artists

Retrieve information about artists related to a specific search query.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Search Playlists
Retrieve information about playlists related to a specific search query.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Search Songs

Retrieve information about songs related to a specific search query.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Search Videos

Retrieve information about videos related to a specific search query.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Search Suggestions

Retrieve a list of search suggestions.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Song

Retrieve information about a song/video.

<details>
<summary>View Example</summary>
<p>

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

</p>
</details>

## Method - Watch

Retrieve information about a song/playlist being watched.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

## Method - Watch Radio

Retrieve information about a song/playlist being watched in radio mode.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

## Method - Watch Shuffle
Retrieve information about a playlist being watched in shuffle mode.

<details>
<summary>View Example</summary>
<p>

```python
>>> # TODO
```

</p>
</details>

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
