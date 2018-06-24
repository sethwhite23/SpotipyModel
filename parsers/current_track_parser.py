from album_parser import AlbumParser
from model.current_track import CurrentTrack
from model.song import Song

class CurrentTrackParser:

    parser_type = "CurrentTrack" #?

    def __init__(self, response):
        self.response = response

    def parse(self):
        progress = self.response["progress_ms"]
        item = self.response['item']
        name = item["name"]
        length = item["duration_ms"]
        album_response = item["album"]
        album = AlbumParser(album_response).parse()
        song = Song(name, album.artists, album, length)
        current_track = CurrentTrack(song, progress)

        return current_track 
