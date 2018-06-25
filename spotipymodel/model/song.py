from artist import Artist
from album import Album

class Song:
    def __init__(self, name, artists, album, length):
        self.name = name
        self.artists = artists
        self.album = album
        self.length = length

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)
