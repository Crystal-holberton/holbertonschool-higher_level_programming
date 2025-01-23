#!/usr/bin/python3
"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """

    Args:
        matrix (list): must be a list of lists of integers or floats
        div (int/float): the divisor
        
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if rows of the matrix are not of the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
        
    Returns:
        List: a new matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
