import pprint

from clients.spotify_client import SpotifyAPI

client_id = '***************'           # your client id
client_secret = '***************'   # your client  secret


spotify = SpotifyAPI(client_id, client_secret)
spotify.perform_auth()
s = spotify.search({"track": "A lennister always pays his debts",
                    "artist": "Ramin"}, search_type='track')
# s = spotify.search(query='Time', operator='not',
#                    operator_query='Billie Elish', search_type='track')
pprint.pprint(s)
