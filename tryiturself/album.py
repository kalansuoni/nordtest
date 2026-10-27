def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


album1 = make_album("Apex Twin", "Richard D. James Album")
album2 = make_album("The Tuss", "Rushup Edge")
album3 = make_album("Caustic Window", "Caustic Window LP")

print(album1)
print(album2)
print(album3)


album4 = make_album("Aphex Twin", "...I Care Because You Do", 20)

print(album4)

def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    return album


while True:
    print("\nEnter album information ('quit' at any time to exit).")

    artist = input("Artist name: ")
    if artist.lower() == "quit":
        break

    title = input("Album title: ")
    if title.lower() == "quit":
        break

    album = make_album(artist, title)
    print(album)