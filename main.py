import spotipy
import spotipy.util as util

from pprint import pprint

token = util.prompt_for_user_token("kylemikableh", show_dialog=False)
sp = spotipy.Spotify(token)
pprint(sp.me())

# Shows playing devices
res = sp.devices()
pprint(res)

sp.start_playback(uris=['spotify:track:1V4jC0vJ5525lEF1bFgPX2'])
sp.volume(100)

#Request Token URL
#https://accounts.spotify.com/authorize?response_type=code&client_id=f9c2918fd0f8419e95f94d9141c3d984&scope=user-read-private,user-read-playback-state,user-modify-playback-state&redirect_uri=http://127.0.0.1
