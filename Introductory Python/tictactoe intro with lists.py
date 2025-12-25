# tuple can't be used because tuple is immutable, use a 3x3 list
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
print(type(game))

for row in game: 
    print(row)