import sys
from spotipymodel import spm

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()


sp = SPM(username)

print sp.current_track()
