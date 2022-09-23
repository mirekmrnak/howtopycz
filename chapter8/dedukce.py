# Určete hodnoty proměnných junk, a, b tak, aby po naznačených úkonech měl seznam junk hodnotu stejnou jako na posledním řádku:
"""
   >>> 13 in junk
   True
   >>> del junk[4]
   >>> junk
   [3, 7, 9, 10, 13, 17, 21, 24, 27]
   >>> del junk[a:b]
   >>> junk
   [3, 7, 27]
"""
# --> del junk[a:b] == del junk[2:-1]

# Nakreslete schema seznamu nlist, do kterého doplníte dále uvedené hodoty 0, 17, 5:
"""
   >>> nlist[2][1]
   0
   >>> nlist[0][2]
   17
   >>> nlist[1][1]
   5
"""
nlist = [
    [0, 0, 17],
    [0, 5, 0],
    [0, 0, 0]
]

# Podle výstupu z metody .split() sestavte hodnotu proměnné retiazka:
"""
   >>> retiazka.split()
   ['this', 'and', 'that']
"""
retiazka = 'this and that'