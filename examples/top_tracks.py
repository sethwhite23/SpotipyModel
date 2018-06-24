import sys
from sp_requests.top_tracks import TopTracksRequest
from model.top_tracks import TopTracks

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

top_tracks = TopTracksRequest(username).issue()
print top_tracks
