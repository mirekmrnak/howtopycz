def compare(x,y):
    if x < y :
        return -1
    elif x > y :
        return 1
    else:
        return 0 

print(compare(1,3), compare(3,3), compare(3,1))