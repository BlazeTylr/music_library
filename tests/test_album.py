from lib.album import *

"""
Album constructs with an id, title and release_year
"""
def test_album_constructs():
    album = Album(1, 'Test Album', 2249)
    assert album.id == 1
    assert album.title == 'Test Album'
    assert album.release_year == 2249