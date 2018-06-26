from sp_request import SPRequest
from ..parsers.current_track_parser import CurrentTrackParser
from ..model.current_track import CurrentTrack

class CurrentTrackRequest(SPRequest):

    scope = 'user-read-currently-playing'

    def _issue(self, sp_client):
        response = sp_client.current_user_playing_track()
        return CurrentTrackParser(response).parse()
