from artist_parser import ArtistParser
from album_parser import AlbumParser
from ..model.album import Album
from ..model.artist import Artist
from ..model.song import Song

class SongParser:
    parser_type = 'track'

    def __init__(self, response):
        self.response = response

    def parse(self):
        name = self.response['name']
        length = self.response['duration_ms']
        album = None
        artists = None
        if 'album' in self.response:
            album = AlbumParser(self.response['album'])
            self.album = album
        
        if 'artists' in self.response:
            artists = []
            for artist_response in self.response['artists']:
                artists.append(ArtistParser(artist_response).parse())
            artists = artists

        song = Song(name, artists, album, length)
        return song
