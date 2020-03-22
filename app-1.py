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
# api  = ytm.AbstractYouTubeMusic()
api = ytm.YouTubeMusic()

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
playlist_id = 'RDCLAK5uy_mkLtojKLOUUGwnu3ZnN5AaODijlieB-aQ'
playlist_id = 'PL4fGSI1pDJn688ebB8czINn0_nov50e3A' # top 100
playlist_id = 'RDCLAK5uy_m1oO6GcuiUbkB7zVErype6l8vOHQ_vh4g' # cuddling country, 100+
playlist_id = 'RDCLAK5uy_nG4p6ReP1bUQMziVrlScqMmElbc7ZqSfk' # has explicit
#video_id = 'q0hyYWKXF0Q' # dance monkey: video
#video_id = 'Hx4nWW9z0ig' # dance monkey: song
# d = api.song_info(video_id)
# data = api.home()
# d=data
album_id = 'OLAK5uy_neMqoK4zw4CrfjMOoy0CjdmZwQTBG3jCA'
# album_id = 'OLAK5uy_m_ThFBkG5CpG5OwA451_2uT6PUv7PMq1A'
# album_id = 'OLAK5uy_l_Ss11gFagXVI_H11IFkoZYNqnQR5WCc8'

# d = api.guide()
# d = api.search_suggestions('foo')
# d = api.hotlist()
# d = api.song_info(song_id='e4Qy-NTKiUQ')
# d = api.home()
# n = d.next()
# d = api.playlist('VLPL4fGSI1pDJn688ebB8czINn0_nov50e3A')
# d = api.playlist('VL' + 'RDCLAK5uy_kT8OSioa9yCqsnqdfvCHOXZUXuLowNT2M')
# d = api.album('OLAK5uy_krJ2XhKRBiQnygRP6n76hbNk_RcmNfkFw')
d = api.search('foo')
# d = api.playlist('VL' + 'RDCLAK5uy_m1oO6GcuiUbkB7zVErype6l8vOHQ_vh4g')
# d2 = d.next()
# artist_id = 'UCMO-CgAtd1jI2m2CrXcP2sQ'
# d = api.base.next(params='mgMDCNgE', player_params='igMDCNgE', video_id=video_id)
# d = api.base.browse_artist(artist_id)
# d = api.search('fuck you')
# d2 = api.search('fuck you', params=d['results']['videos']['params'])
# d3 = api.search(continuation=d2['continuation'])
# x=d['contents']['singleColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']

# d = api.album(album_id=album_id)

# Note: Shuffle and Radio can be passed through as Arguments
# E.g: playlist = api.radio(song_id or playlist_id or album_id)

#
# data2 = api.home(continuation=d['continuation'])
# d2=data2
# d = api.hotlist()
# d = api.guide()
# d = api.playlist(playlist_id)
# pp(d)
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
