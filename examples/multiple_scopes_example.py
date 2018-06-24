import sys
from model.spm import SPM

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

scopes = 'user-library-read user-top-read user-read-currently-playing'
sp = SPM(username, scopes)

print "Top Artists:\n" + str(sp.top_artists()) + "\n"
print "Current Track:\n" + str(sp.current_track()) + "\n"
