# python-youtube-music

Unofficial Python YouTube Music Web API Client

** **Still under active development** **

![YouTube Music](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Logo_of_YouTube_Music.svg/1280px-Logo_of_YouTube_Music.svg.png)

## Dependencies
[requests](https://github.com/psf/requests) >= 2.18.2

[youtube_dl](https://github.com/ytdl-org/youtube-dl) >= 2020.03.24 (optional)

## Installation

### From Source
Clone this repository and run setup.py:
```
cd python-youtube-music && python setup.py install
```

## Getting Started
Initialise a YouTubeMusic instance
```python
import ytm

api = ytm.YouTubeMusic()
```
