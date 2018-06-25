from artist import Artist

class TopArtists:

    def __init__(self, artists):
        self.artists = artists

    def __str__(self):
        s = ""
        for i, artist in enumerate(self.artists):
            s += str(i+1) + ". " + artist.name + "\n"
        return s
