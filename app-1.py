import ytm
# import ytm.utils
from ytm import utils
# import ytm.apis
# from type_shell import type_shell
# import youtube_dl

from pprint import pprint as pp
gn = utils.get_nested
ytm_utils=utils

bapi = ytm.BaseYouTubeMusic()
api  = ytm.AbstractYouTubeMusic()

'''
# Remember, aim is also to make a REST api for each: So each should have dump as dict

api = ytm.YouTubeMusic()
home = api.home()

.home()    : Home page and browse
.hotlist() : Hotlist page and browse
.search()  : Search page and api resp
.playlist(): Playlist page and resp
.artist()  : Artist page and resp
.song()    : Song page and resp
.song_info(): Video info?
.album()   : Album page and resp
.guide()   : Guide page and resp
.search_suggestions(): Search suggestions
'''

# d = api.search_suggestions('foo')
# d = api.song_info('q0hyYWKXF0Q')
video_id = '8zZHAfq0gls' # aquilo, sober
#video_id = 'q0hyYWKXF0Q' # dance monkey: video
#video_id = 'Hx4nWW9z0ig' # dance monkey: song
# d = api.song_info(video_id)
# data = api.home()
# d=data
#
# data2 = api.home(continuation=d['continuation'])
# d2=data2
d = api.hotlist()
pp(d)
# x = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer')
# x=ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', default = [])[:-1]
# pp(d)
# opts = \
# {
#     'format': 'bestaudio/best',
# }
# with youtube_dl.YoutubeDL(opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=' + video_id])

# w = d['watch_next_response']
# p = d['player_response']
# w = d['_x']

# x = w['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]

# pp

# print('\n')

# for k, v in d.items():
#     print(k.ljust(35), str(type(v)).ljust(10), repr(v)[:100])

# x = d['INITIAL_ENDPOINT']['browseEndpoint']['browseId']

# pp(d)

# pp(d)

# d = {'foo': [{'bar': 1}]}
#
# type_shell(d)
