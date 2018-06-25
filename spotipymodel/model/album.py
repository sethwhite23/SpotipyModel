from artist import Artist

class Album:
    def __init__(self, name, artists):
        self.name = name
        self.artists = artists

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)
