from song_parser import SongParser
from model.song import Song
from model.top_tracks import TopTracks
from pprint import pprint

class TopTracksParser:

    parser_type = "TopTracks" #?

    def __init__(self, response):
        self.response = response

    def parse(self):
        items = self.response['items']
        songs = []
        for item in items:
            song = SongParser(item).parse()
            songs.append(song)

        top_tracks = TopTracks(songs)
        return top_tracks  
