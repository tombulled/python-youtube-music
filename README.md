# python-youtube-music

![Made With Python](https://forthebadge.com/images/badges/made-with-python.svg)
![Built By Neckbeards](https://forthebadge.com/images/badges/built-by-neckbeards.svg)
![Gluten Free](https://forthebadge.com/images/badges/gluten-free.svg)  
![Forks](https://img.shields.io/github/forks/tombulled/python-youtube-music?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/tombulled/python-youtube-music?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/tombulled/python-youtube-music?style=for-the-badge)
![License](https://img.shields.io/github/license/tombulled/python-youtube-music?style=for-the-badge)

Python YouTube Music Web API Client - **Still under active development** - _Nearly at v1.0_   :smile:

![YouTube Music](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Logo_of_YouTube_Music.svg/1280px-Logo_of_YouTube_Music.svg.png)

## Contents:
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Getting Started](#getting-started)
* [Methods](#methods)
<!-- * [Roadmap](#roadmap) -->

## Dependencies
Libraries ```ytm``` depends on

### Required Dependencies
| Library                                     | Install              | Import          | Functionality            |
| ------------------------------------------- | -------------------- | --------------- | ------------------------ |
| [Requests](https://github.com/psf/requests) | pip install requests | import requests | Send HTTP/HTTPS requests |

### Optional Dependencies
| Library                                                 | Install                | Import            | Functionality                |
| ------------------------------------------------------- | ---------------------- | ----------------- | ---------------------------- |
| [YoutubeDL](https://github.com/ytdl-org/youtube-dl)     | pip install youtube-dl | import youtube_dl | Download YouTube videos      |
| [Mutagen](https://github.com/quodlibet/mutagen)         | pip install mutagen    | import mutagen    | Read and write audio metadata|
| [Pillow (PIL)](https://github.com/python-pillow/Pillow) | pip install Pillow     | import PIL        | Python imaging library       |

## Installation
Install ```ytm``` onto your system.

<!--
### Install From PyPi
In a terminal execute:

```console
user@host:~$ pip install ytm # You may need to use: python3 -m pip install ytm
Successfully installed ytm
```
-->

### Install From Source
Firstly, clone or download this repository.

#### Basic Installation:
No YouTubeMusicDL support
```console
user@host:~$ pip install . # You may need to use: python3 -m pip install .
Successfully installed ytm
```

#### Full Installation:
YouTubeMusicDL support
```console
user@host:~$ pip install .[dl] # You may need to use: python3 -m pip install .[dl]
Successfully installed ytm
```

<!--
## Roadmap
Things still left to do:
* Documentation: Will live on GitHub Wiki
* Landing page: Will live on GitHub Pages Page
* CLI: YouTubeMusicDL command-line interface invoked by - python -m ytm --foo --bar
-->

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
['album',
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

## Methods
API methods available to retrieve data from YouTube Music:

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

### Method - Album

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

### Method - Artist

Retrieve information about an artist.

<details>
<summary>View Example</summary>
<p>

```python
>>> artist = api.artist('UC8Yu1_yfN5qPh601Y4btsYw') # Arctic Monkeys
>>>
>>> list(artist)
['name', 'id', 'subscribers', 'views', 'description', 'albums', 'singles', 'videos', 'songs', 'playlists', 'similar_artists']
>>>
>>> artist['name']
'Arctic Monkeys'
>>> artist['subscribers']
'4.34M'
>>> artist['views']
2082236489
>>> artist['description']
'For tour dates, visit the website www.arcticmonkeys.com'
>>>
```

</p>
</details>

### Method - Artist Albums

Retrieve information about an artist's albums.

<details>
<summary>View Example</summary>
<p>

```python
>>> artist = api.artist('UC8Yu1_yfN5qPh601Y4btsYw') # Arctic Monkeys
>>>
>>> artist_id = artist['id']
>>> params = artist['albums']['params']
>>>
>>> albums = api.artist_albums(artist_id, params)
>>>
>>> for album in albums:
	print(album['name'])

Tranquility Base Hotel & Casino
AM
Suck It and See
My Propeller
Cornerstone
Humbug
Teddy Picker
Fluorescent Adolescent
Favourite Worst Nightmare
Brianstorm
Who The Fuck Are Arctic Monkeys?
Whatever People Say I Am, That's What I Am Not
>>>
```

</p>
</details>

### Method - Artist Singles

Retrieve information about an artist's singles.

<details>
<summary>View Example</summary>
<p>

```python
>>> artist = api.artist('UC8Yu1_yfN5qPh601Y4btsYw') # Arctic Monkeys
>>>
>>> artist_id = artist['id']
>>> params = artist['singles']['params']
>>>
>>> singles = api.artist_singles(artist_id, params)
>>>
>>> for single in singles:
	print(single['name'])

Tranquility Base Hotel & Casino
Why'd You Only Call Me When You're High?
Do I Wanna Know?
One For The Road
R U Mine? / Electricity
Black Treacle
Suck It And See
The Hellcat Spangled Shalalala
Don't Sit Down 'Cause I've Moved Your Chair
Crying Lightning
Da Frame 2R / Matador
Leave Before The Lights Come On
When The Sun Goes Down
I Bet You Look Good On The Dancefloor
>>>
```

</p>
</details>

### Method - Guide

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

### Method - Home

Retrieve information about shelves displayed on the home page.

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

### Method - Hotlist
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

### Method - Playlist
Retrieve information about a playlist.

<details>
<summary>View Example</summary>
<p>

```python
>>> playlist = api.playlist('RDCLAK5uy_lXWhlJsihey6xq1b50d7Uv93NLqle8TSc')
>>>
>>> list(playlist)
['name', 'type', 'year', 'thumbnail', 'duration', 'id', 'total_tracks', 'artist', 'radio', 'shuffle', 'tracks', 'continuation']
>>>
>>> playlist['name']
'Take It Easy Indie'
>>> playlist['year']
2020
>>> playlist['duration']
'6+ hours'
>>> playlist['total_tracks']
163
>>>
>>> for track in playlist['tracks'][:5]: # First 5 Tracks
	print(track['artist']['name'], '-', track['name'])


Lord Huron - The Night We Met (feat. Phoebe Bridgers)
The Lumineers - Cleopatra
The xx - I Dare You
Hozier - Work Song
girl in red - we fell in love in october
>>>
>>> # Continue Data
>>> playlist2 = api.playlist(continuation = playlist['continuation'])
>>>
>>> for track in playlist2['tracks'][:5]: # First 5 Tracks
	print(track['artist']['name'], '-', track['name'])


Maddie Jay - Mood Swings
Cloud Control - Dojo Rising
Broken Bells - The Angel and the Fool
George Glew - Bittersweet
Cold War Kids - First
>>>
```

</p>
</details>

### Method - Search

Retrieve information about a specific search.

<details>
<summary>View Example</summary>
<p>

```python
>>> results = api.search('alt-j')
>>>
>>> list(results)
['albums', 'playlists', 'videos', 'artists', 'songs', 'top_results']
>>>
>>> results['top_results']
'artists'
>>>
>>> results['artists'][0]['name']
'alt-J'
>>>
>>> results['albums'][0]['name']
'An Awesome Wave'
>>>
>>> results[results['top_results']][0]['name']
'alt-J'
>>>
```

</p>
</details>

### Method - Search Albums
Retrieve information about albums related to a specific search query.

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

### Method - Search Artists

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

### Method - Search Playlists
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

### Method - Search Songs

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

### Method - Search Videos

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

### Method - Search Suggestions

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

### Method - Song

Retrieve information about a song/video.

<details>
<summary>View Example</summary>
<p>

```python
>>> song = api.song('pPt_FZ9m2bM')
>>>
>>> list(song)
['rating', 'duration', 'description', 'thumbnail', 'name', 'id', 'views', 'dislikes', 'likes', 'explicit', 'recommended', 'date', 'artist']
>>>
>>> song['name']
'The Key to Life on Earth'
>>> song['artist']['name']
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
>>> for track in song['recommended'][:5]: # First 5 Tracks
	print(track['artist']['name'], '-', track['name'])

Declan McKenna - British Bombs
None - Mix - The Key to Life on Earth
Declan McKenna - Beautiful Faces
Declan McKenna - Declan McKenna - The Key to Life on Earth (Official Video)
Will Joseph Cook - Will Joseph Cook - Girls Like Me
>>>
```

</p>
</details>

### Method - Watch

Retrieve information about a song/playlist being watched.

<details>
<summary>View Example</summary>
<p>

```python
>>> watch = api.watch('dIwwjy4slI8', 'RDCLAK5uy_mgonaF5RiN90kqT-edkFB53N81dZ9XHp8')
>>>
>>> list(watch)
['id', 'name', 'continuation', 'total', 'tracks', 'radio', 'current']
>>>
>>> watch['name']
'Celestial Instrumentals'
>>> watch['total']
52
>>> watch['radio']
False
>>>
>>> for track in watch['tracks'][:5]: # First 5 tracks
	print(track['name'])

Says
The Light
Sun Drugs
Dark Lights
Together Alone
>>>
>>> # Continue data
>>> watch2 = api.watch(continuation = watch['continuation'])
>>>
>>> for track in watch2['tracks'][:5]: # First 5 tracks
	print(track['name'])

Goodnight
Indoor Swimming At The Space Station
Hoppípolla
Sleeping on the Roof
Zero Gravity
```

</p>
</details>

### Method - Watch Radio

Retrieve information about a song/playlist being watched in radio mode.

<details>
<summary>View Example</summary>
<p>

```python
>>> song_radio = api.watch_radio(song_id = '8A9_1hGmtj0')
>>>
>>> list(song_radio)
['id', 'name', 'continuation', 'total', 'tracks', 'radio', 'current']
>>>
>>> song_radio['id']
'RDAMVM8A9_1hGmtj0'
>>>
>>> for track in song_radio['tracks'][:5]: # First 5 Tracks
	print(track['name'])

Travel Is Dangerous
A Gallant Gentleman
Motion Picture Soundtrack
Don't Stay Here
Everything In Its Right Place
>>>
>>> playlist_radio = api.watch_radio(playlist_id = 'RDCLAK5uy_kNj0whsN9sFy3dqiTCfu34HoOdeZIjfyw')
>>>
>>> list(playlist_radio)
['id', 'name', 'continuation', 'total', 'tracks', 'radio', 'current']
>>>
>>> playlist_radio['id']
'RDAMPLRDCLAK5uy_kNj0whsN9sFy3dqiTCfu34HoOdeZIjfyw'
>>> playlist_radio['name']
'Ambient Post Rock'
>>>
>>> for track in playlist_radio['tracks'][:5]: # First 5 Tracks
	print(track['name'])

Only The Winds
The Winter
The Kindness In Letting Go
Aldgate Patterns
I'm Not
>>>
```

</p>
</details>

### Method - Watch Shuffle
Retrieve information about a playlist being watched in shuffle mode.

<details>
<summary>View Example</summary>
<p>

```python
>>> watch = api.watch_shuffle('RDCLAK5uy_l6Wg_lE2_Wx7GdOE21bKJvYPIif8n1fAQ')
>>>
>>> list(watch)
['id', 'name', 'continuation', 'total', 'tracks', 'radio', 'current']
>>>
>>> watch['name']
'Peaceful Indie Dreams'
>>>
>>> for track in watch['tracks'][:5]: # First 5 Tracks
	print(track['name'])

Make It Holy
Bible Belt (Acoustic)
Take Care
Atlas Hands
Sweetheart, What Have You Done to Us
>>>
```

</p>
</details>
