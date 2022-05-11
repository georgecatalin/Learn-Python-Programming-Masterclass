
# to recognize nested tuples inside the list, these have to be enclosed in parentheses
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lightning", "Metallica", 1984)]


print(len(albums))

# an example of unpacking the list with nested tuples
for album in albums:
    print("Album: Song {0}, Band {1}, Year {2} ".format(album[0], album[1], album[2]))

# a much clearer example of unpacking the list with nested tuples
for album in albums:
    song, band, year = album
    print("Album: Song {0}, Band {1}, Year {2}".format(song,band,year))