import spotipy
import spotipy.util as util

class SPRequest:

    scope = None

    def __init__(self, username, scopes = None):
        self.username = username
        self.scopes = scopes

    def issue(self):
            sp = self.sp_client()
            return self._issue(sp)

    def _issue(self, sp_client):
        pass

    def _scopes(self):
        if self.scopes:
            return self.scopes
        return self.scope

    def sp_client(self):
        token = util.prompt_for_user_token(self.username, self._scopes())

        if token:
            sp = spotipy.Spotify(auth=token)
            return sp
        return None
