def compare(x,y):
    if x < y :
        print(x, "je menší než", y)
    elif x > y :
        print(x, "je větší než", y)
    else:
        print(f'{x} a {y} jsou stejné') #použití 

compare(1,3)
compare(3,3)
compare(3,1)