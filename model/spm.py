from sp_requests.top_tracks import TopTracksRequest
from sp_requests.top_artists import TopArtistsRequest
from sp_requests.current_track import CurrentTrackRequest

class SPM:
    
    def __init__(self, user, scopes = None):
        self.user = user
        self.scopes = scopes

    def top_tracks(self):
        return TopTracksRequest(self.user, scopes = self.scopes).issue()

    def top_artists(self):
        return TopArtistsRequest(self.user, scopes = self.scopes).issue()

    def current_track(self):
        return CurrentTrackRequest(self.user, scopes = self.scopes).issue()
