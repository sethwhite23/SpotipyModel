from sp_request import SPRequest
from parsers.top_tracks_parser import TopTracksParser
from model.top_tracks import TopTracks

class TopTracksRequest(SPRequest):

    scope = 'user-top-read'

    def _issue(self, sp_client):
        response = sp_client.current_user_top_tracks()
        return TopTracksParser(response).parse()
