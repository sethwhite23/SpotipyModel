from sp_request import SPRequest
from ..parsers.top_artists_parser import TopArtistsParser
from ..model.top_tracks import TopTracks

class TopArtistsRequest(SPRequest):

    scope = 'user-top-read'

    def _issue(self, sp_client):
        response = sp_client.current_user_top_artists()
        return TopArtistsParser(response).parse()
