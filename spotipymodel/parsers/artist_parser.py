from ..model.artist import Artist

class ArtistParser:
    parser_type = 'artist'

    def __init__(self, response):
        self.response = response


    def parse(self):
        name = self.response['name']
        artist = Artist(name)
        return artist
