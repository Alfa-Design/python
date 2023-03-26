#Working with Part of a List


#Slicing a List
players = ['john', 'mike', 'cuzo', 'pythons', 'duma', 'dest' 'charles', 'martina', 'michael', 'florence', 'eli']
"""
print(players[2:4])
print(players[:4])
print(players[-4:])
print(players[2:])
"""

#Looping Through a Slice
for player in players[3:6]:
    print(player.title())