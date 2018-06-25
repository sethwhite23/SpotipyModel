from artist import Artist
from album import Album

class CurrentTrack:

    def __init__(self, song, progress):
        self.song = song
        self.progress = progress

    def __str__(self):
        artists = self.song.artists
        artists_names = []
        for artist in artists:
            artists_names.append(artist.name)
        artists_names_str = " & ".join(artists_names)

        return self.song.name + ' - '  + artists_names_str + ' - ' + self.song.album.name
