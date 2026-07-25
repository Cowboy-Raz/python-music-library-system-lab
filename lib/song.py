class Song:
    """Represents a song and tracks library-wide song data."""
 
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
 
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
 
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)
 
    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs created."""
        cls.count += 1
 
    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the set of all known genres (no duplicates)."""
        cls.genres.add(genre)
 
    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the set of all known artists (no duplicates)."""
        cls.artists.add(artist)
 
    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment this genre's count, starting it at 1 if it's new."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
 
    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment this artist's count, starting it at 1 if it's new."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1