import ytm
# import ytm.utils
from ytm import utils
from ytm import constants
# import ytm.apis
# from type_shell import type_shell
# import youtube_dl

from pprint import pprint as pp
gn = utils.get_nested
ytm_utils=utils
ytm_constants=constants

bapi = ytm.BaseYouTubeMusic()
# api  = ytm.AbstractYouTubeMusic()
api = ytm.YouTubeMusic()
aapi = ytm.AbstractYouTubeMusic()

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

'''
api = ytm.YouTubeMusic()

search = api.search('foo fighters')
songs = search.filter_songs()
song = songs[0]
artist = song.artist()
album = artist['albums'][0].album()
track = album['tracks'][0]
'''

# d = api.search_suggestions('foo')
# d = api.song_info('q0hyYWKXF0Q')
video_id    = '8zZHAfq0gls' # aquilo, sober
playlist_id = 'PL4fGSI1pDJn688ebB8czINn0_nov50e3A' # top 100
playlist_id = 'RDCLAK5uy_m1oO6GcuiUbkB7zVErype6l8vOHQ_vh4g' # cuddling country, 100+
playlist_id = 'RDCLAK5uy_mkLtojKLOUUGwnu3ZnN5AaODijlieB-aQ'
album_id = 'OLAK5uy_kAl2X0kHMaNH_FkOL2q8KZ5mrONEzSpxA' # Has songs feat.
album_id = 'OLAK5uy_mD8Zx-hl4LY7cs5ia8IMvguvtphKvKlR0' # Single track has feat.
album_id = 'OLAK5uy_lEX2ZWJ-FoqZ3jcWIGciMFASauDCOAiEA' # Madeon
album_id = 'OLAK5uy_l_d-om0EjO1rBK11kFEDwUC3VZL07D1EA' # EP
album_id = 'OLAK5uy_lH7XpeHbWduEtZ1PdCOaH5yRuRD0Ppm3U' # Has 'other versions'
# playlist_id = 'RDCLAK5uy_nG4p6ReP1bUQMziVrlScqMmElbc7ZqSfk' # has explicit
#video_id = 'q0hyYWKXF0Q' # dance monkey: video
#video_id = 'Hx4nWW9z0ig' # dance monkey: song
# d = aapi.playlist(playlist_id)
# d = aapi.album(album_id)
d = aapi.search('cocoon')
# d = aapi.search_videos('cocoon')
# d = aapi.search_artists('amber run')
# d = aapi.search_songs('cocoon')
# d = api.search('amber run')
# d = aapi.search_albums('aim and ignite')
# d = aapi.search_playlists('indie') # Bugged !!
# d = api.song_info(video_id)
# d = aapi.guide()
# d = aapi.hotlist()
# d = aapi.song(video_id)
# d = api.next(video_id)
# d = aapi.suggest('foo')
# d = aapi.watch(video_id)
# d2 = aapi.watch(continuation=d['playlist']['continuation'])
# d2 = aapi.watch \
# (
#     song_id = d['playlist']['tracks'][1]['id'],
#     playlist_id = d['playlist']['id'],
# )
# d = aapi.home()
# with open('out.html', 'w') as file: file.write(str(d))
# d = api.base.browse(browse_id='VLOLAK5uy_l522aR1P2og1g1mGZkwU_gJj5HKWrjFfU', page_type = ytm_constants.PAGE_TYPE_PLAYLIST)
# d = api.playlist(playlist_id='OLAK5uy_l522aR1P2og1g1mGZkwU_gJj5HKWrjFfU')
# d=data
# album_id = 'OLAK5uy_neMqoK4zw4CrfjMOoy0CjdmZwQTBG3jCA'
# album_id = 'OLAK5uy_m_ThFBkG5CpG5OwA451_2uT6PUv7PMq1A'
# album_id = 'OLAK5uy_l_Ss11gFagXVI_H11IFkoZYNqnQR5WCc8'

# d = api.watch(song_id='hwGBYGexu_I', playlist_id='PLeagXyg528O4QWuQRhOyN4qpXhltbYOLc')
# d = api.artist('UCMO-CgAtd1jI2m2CrXcP2sQ')
# d = api.artist('UCmAgTXAlnckJJBFmqYlHnNA')
# a = d['shelves']['albums'] # ['items'][0]
# x = a.next()
# s = d['shelves']['singles']
# x = s.next()
# d = api.watch(song_id='ItHnOBApqI4', playlist_id='RDEMl1OPQXVBv7sXQEeqlL1HZg')
# d = api.guide()
# d = api.search_suggestions('foo')
# d = api.hotlist()
# d = api.song_info(song_id='e4Qy-NTKiUQ')
# d = api.home()
# n = d.next()
# d = api.playlist('VLPL4fGSI1pDJn688ebB8czINn0_nov50e3A')
# d = api.playlist('VL' + 'RDCLAK5uy_kT8OSioa9yCqsnqdfvCHOXZUXuLowNT2M')
# d = api.album('OLAK5uy_krJ2XhKRBiQnygRP6n76hbNk_RcmNfkFw')
# d = api.search('amber run')
# d2 = d.filter_albums()
# d3 = d2.next()
# print(len(d['results']['videos']['items']))
# d2 = d.filter_videos()
# print(len(d['results']['videos']['items']))

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
