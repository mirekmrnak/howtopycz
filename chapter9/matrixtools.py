from copy import deepcopy
#Pro následující doctesty vytvořte záhlaví a těla funkcí, které přidají řádek, případně sloupec do zadané matice.
def add_row (matrix): 
    """
    >>> m = [[0,0], [0,0]] 
    >>> add_row(m)    
    [[0, 0], [0, 0], [0, 0]]
    >>> n = [[3, 2, 5], [1, 4, 7]]
    >>> add_row(n)
    [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
    >>> n
    [[3, 2, 5], [1, 4, 7]]
    """
    new_matrix = matrix.copy()
    new_matrix.append([0 for i in matrix[0]])
    return new_matrix

def add_column (matrix): 
    """
    >>> m = [[0, 0], [0, 0]] 
    >>> add_column(m)    
    [[0, 0, 0], [0, 0, 0]]
    >>> n = [[3, 2], [5, 1], [4, 7]]
    >>> add_column(n)
    [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
    >>> n
    [[3, 2], [5, 1], [4, 7]]
    """
    new_matrix = deepcopy(matrix)
    for i in new_matrix:
        i.append(0)

    return new_matrix

# Napište funkci add_matrices(m1, m2), která vrátí novou matici, jež je součtem matic m1 a m2. Sečíst dvě matice znamená sečíst hodnoty odpovídajících členů. Můžete předpokládat, že matice m1 a m2 mají stejnou velikost.
def add_matrices (m1, m2): 
    """
    >>> a = [[1,2], [3,4]]
    >>> b = [[2,2], [2,2]] 
    >>> add_matrices(a, b)    
    [[3, 4], [5, 6]]
    >>> c = [[8,2], [3,4], [5,7]]
    >>> d = [[3,2], [9,2], [10,12]]
    >>> add_matrices(c, d)
    [[11, 4], [12, 6], [15, 19]]
    >>> c
    [[8, 2], [3, 4], [5, 7]]
    >>> d
    [[3, 2], [9, 2], [10, 12]]
    """
    #kombinace list comprehansion a klasiky
    lst = []
    for i in range(len(m1)):
        lst.append([m1[i][j]+m2[i][j] for j in range(len(m1[0]))])
    return lst

# Napište funkci scalar_mult(n, m), která násobí matici m skalárem n. Doplňte tělo funkce a ujistěte se, že projde doctesty.
def scalar_mult (n, m): 
    """
    >>> a = [[1,2], [3,4]]
    >>> scalar_mult(3, a)    
    [[3, 6], [9, 12]]
    >>> b = [[3,5,7], [1,1,1], [0,2,0], [2,2,3]]
    >>> scalar_mult(10, b)
    [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
    >>> b
    [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    lst = []
    for i in range(len(m)):
        lst.append([m[i][j]*n for j in range(len(m[0]))])
    return lst

# Na základě získané zkušenosti zkuste násobit matici maticí.
def matrix_mult (m1, m2): 
    """
    | 1 2 | * | 5 6 |     1*5 + 2*7 | 1*6 + 2*8     | 19 22 |
    |     |   |     |  =  ----------|----------  =  |       |
    | 3 4 |   | 7 8 |     3*5 + 4*7 | 5*6 + 4*8     | 43 50 |
    >>> matrix_mult([[1,2], [3,4]], [[5,6], [7,8]])
    [[19, 22], [43, 50]]
    >>> matrix_mult([[1,2,3], [4,5,6]], [[7,8], [9,1], [2,3]])
    [[31, 19], [85, 55]]
    >>> matrix_mult([[7,8], [9,1], [2,3]], [[1,2,3], [4,5,6]])
    [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    new_matrix = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                new_matrix[i][j] += (m1[i][k]*m2[k][j])
    return new_matrix

if __name__ == '__main__':
    import doctest
    doctest.testmod()