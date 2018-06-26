from artist_parser import ArtistParser
from ..model.artist import Artist
from ..model.top_artists import TopArtists

class TopArtistsParser:

    parser_type = "TopArtists" #?

    def __init__(self, response):
        self.response = response

    def parse(self):
        items = self.response['items']
        artists = []
        for item in items:
            artist = ArtistParser(item).parse()
            artists.append(artist)

        top_artists = TopArtists(artists)
        return top_artists
