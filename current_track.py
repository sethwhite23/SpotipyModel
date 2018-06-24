import sys
from sp_requests.current_track import CurrentTrackRequest

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

current_track = CurrentTrackRequest(username).issue()
print current_track
