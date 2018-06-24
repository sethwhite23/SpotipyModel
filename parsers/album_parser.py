from artist_parser import ArtistParser
from model.album import Album

class AlbumParser:
    parser_type = 'album'

    def __init__(self, response):
        self.response = response

    def parse(self):
        name = self.response['name']
        artists = []
        artists_response = self.response['artists']
        for artist_response in artists_response:
            artist = ArtistParser(artist_response).parse()
            artists.append(artist)
        album = Album(name, artists)
        return album
