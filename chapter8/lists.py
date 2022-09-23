seznam = ['spam!', 1, ['Brie', [[['Roquefort']]], 'Pol le Veq'], [1, 2, 3]]
seznam2 = [['Brie', 'Roquefort', 'Pol le Veq']]

def lenghts(list):
    delky = []
    for item in list:
        if type(item) == type(1):
            delky.append(len(str(item)))
        elif type(item) == type([]):
            delky += lenghts(item)
        else:
            delky.append(len(item))
    return delky

print(lenghts(seznam))
print(lenghts(seznam2))