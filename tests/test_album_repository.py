from lib.album import *
from lib.album_repository import *

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_albums(db_connection):
    db_connection.seed('seeds/music_library.sql')

    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [Album(1,'Doolittle', 1989), Album(2, 'Surfer Rosa', 1988), Album(3, 'Waterloo', 1974), Album(4, 'Super Trouper', 1980), Album(5, 'Bossanova', 1990), Album(6, 'Lover', 2019), Album(7, 'Folklore', 2020), Album(8, 'I Put a Spell on You', 1965), Album(9, 'Baltimore', 1978), Album(10, 'Here Comes the Sun', 1971), Album(11, 'Fodder on My Wings', 1982), Album(12, 'Ring Ring', 1973)]

