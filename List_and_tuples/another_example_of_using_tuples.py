metallica = "Ride the lightning", "Metallica", 1984

# unpacking a tuple into meaningful data
title, band, year = metallica
print(title)
print(band)
print(year)

piece_of_furniture = "table", 200, 100, 20, 15.6
name, length, width, height, price = piece_of_furniture
print("Unpacking in crazy terms")
# a fuzzy way to unpack
print(piece_of_furniture[1] * piece_of_furniture[2])
# a better way to unpack
print(length * width)
