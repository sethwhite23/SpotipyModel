from song import Song

class TopTracks:

    def __init__(self, songs):
        self.songs = songs

    def __str__(self):
        s = ""
        for i, song in enumerate(self.songs):
            artists = song.artists
            artists_names = []
            for artist in artists:
                artists_names.append(artist.name)
            artists_names_str = " & ".join(artists_names)

            s += str(i+1) + ". " + song.name + ' - ' + artists_names_str + "\n"
        return s
