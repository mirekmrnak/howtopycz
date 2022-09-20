def slope (x1,y1,x2,y2):
    """
    Funkce slope(x1,y1,x2,y2), která vrací tangent úhlu (sklonu) přímky procházející body (x1,y1) a (x2,y2).
    >>> slope(5,3,4,2)
    1.0
    >>> slope(1,2,3,2)
    0.0
    >>> slope(1,4,1,2)         
    "kolmice k ose 'x'"
    >>> slope(2,4,1,2)
    2.0
    """
    if (x2 - x1) == 0:
        return "kolmice k ose 'x'"
    else:
        return ((y2 - y1) / (x2 - x1))

#import math
#print(math.degrees(math.atan(slope(0,0,5,5))))

if __name__ == '__main__':
    import doctest
    doctest.testmod()