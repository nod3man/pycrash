players = ['charles', 'martina', 'michael', 'florence', 'eli']

# First index is start, second index is end. Returns elements from n to m-1
print(players[0:3])
print(players[1:4])

# If first index is ommited then start from beginning of the list ( [:n] = [0:n] )
print(players[:4])

# If second index is ommited then return from n to end of the list ( [:n] = [0:n] )
print(players[2:])

# It is possible to use negative index
print(players[-3:])

print()

# It is possible to loop through slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
