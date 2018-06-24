import sys
from sp_requests.top_artists import TopArtistsRequest

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

top_artists = TopArtistsRequest(username).issue()
print top_artists
