def intercept (x1,y1,x2,y2):
    """
    >>> intercept(1,6,3,12)
    3.0
    >>> intercept(6,1,1,6)
    7.0
    >>> intercept(4,6,12,8)
    5.0
    """
    #obecná rovnice přímky: a*x + b*y + c = 0
    u = (x2-x1, y2-y1) #směrový vektor
    n = (u[1], -u[0]) #normálový vektor
    a, b = n[0], n[1] #parametry rovnice a, b
    c = -a*x1 - b*y1 #dopočet parametru c dosazením bodu na přímce

    #vracíme hodnotu y pro x = 0, tzn. průnik s osou y
    return -c / b

if __name__ == '__main__':
    import doctest
    doctest.testmod()