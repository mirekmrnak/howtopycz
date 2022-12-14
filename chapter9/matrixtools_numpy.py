import numpy as np

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
    np_matrix = np.array(matrix)
    #row = [0 for i in range(len(matrix[0]))]
    #np_matrix = np.append(np_matrix, [row], axis=0)
    np_matrix = np.insert(np_matrix, len(matrix), 0, axis=0)
    return np_matrix.tolist()

def add_column (matrix): 
    """
    >>> m = [[0,0], [0,0]] 
    >>> add_column(m)    
    [[0, 0, 0], [0, 0, 0]]
    >>> n = [[3,2], [5,1], [4,7]]
    >>> add_column(n)
    [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
    >>> n
    [[3, 2], [5, 1], [4, 7]]
    """
    np_matrix = np.array(matrix)
    #column = [[0] for i in range(len(matrix))]
    #np_matrix = np.append(np_matrix, column, axis=1)
    np_matrix = np.insert(np_matrix, len(matrix[0]), 0, axis=1)
    return np_matrix.tolist()

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
    return (np.array(m1, dtype=np.int8) + np.array(m2, dtype=np.int8)).tolist()

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
    return (n * np.array(m, dtype=np.int8)).tolist()

def matrix_mult (m1, m2): 
    """
    >>> matrix_mult([[1,2], [3,4]], [[5,6], [7,8]])
    [[19, 22], [43, 50]]
    >>> matrix_mult([[1,2,3], [4,5,6]], [[7,8], [9,1], [2,3]])
    [[31, 19], [85, 55]]
    >>> matrix_mult([[7,8], [9,1], [2,3]], [[1,2,3], [4,5,6]])
    [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    return (np.array(m1) @ np.array(m2)).tolist() #eventueln?? np.matmul(a, b)

if __name__ == '__main__':
    import doctest
    doctest.testmod()