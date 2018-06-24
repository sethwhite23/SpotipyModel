import spotipy
import spotipy.util as util

class SPRequest:

    scope = None

    def __init__(self, username):
        self.username = username

    def issue(self):
            sp = self.sp_client()
            return self._issue(sp)

    def _issue(self, sp_client):
        pass

    def sp_client(self):
        token = util.prompt_for_user_token(self.username, self.scope)

        if token:
            sp = spotipy.Spotify(auth=token)
            return sp
        return None
