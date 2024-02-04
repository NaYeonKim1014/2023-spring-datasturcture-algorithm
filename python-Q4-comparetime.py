import time

## Standard Multiplication
def standard_multiplication(matrix1, matrix2):
    # Get dimensions of matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if matrices can be multiplied
    if cols1 != rows2:
        raise ValueError("Cannot multiply the matrices. Invalid dimensions.")
    
    # Initialize result matrix
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

## Strassen's Multiplication
def split_matrix(matrix):
    n = len(matrix)
    split = n // 2
    a = [[0 for _ in range(split)] for _ in range(split)]
    b = [[0 for _ in range(split)] for _ in range(split)]
    c = [[0 for _ in range(split)] for _ in range(split)]
    d = [[0 for _ in range(split)] for _ in range(split)]

    for i in range(split):
        for j in range(split):
            a[i][j] = matrix[i][j]
            b[i][j] = matrix[i][j + split]
            c[i][j] = matrix[i + split][j]
            d[i][j] = matrix[i + split][j + split]

    return a, b, c, d


def merge_matrices(a, b, c, d):
    n = len(a)
    merged = [[0 for _ in range(2 * n)] for _ in range(2 * n)]

    for i in range(n):
        for j in range(n):
            merged[i][j] = a[i][j]
            merged[i][j + n] = b[i][j]
            merged[i + n][j] = c[i][j]
            merged[i + n][j + n] = d[i][j]

    return merged


def add_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


def subtract_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] - matrix2[i][j]

    return result


def strassen_multiplication(matrix1, matrix2):
    n = len(matrix1)

    # Base case for recursion
    if n == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    # Split matrices
    a, b, c, d = split_matrix(matrix1)
    e, f, g, h = split_matrix(matrix2)

    # Recursive calls
    p1 = strassen_multiplication(a, subtract_matrices(f, h))
    p2 = strassen_multiplication(add_matrices(a, b), h)
    p3 = strassen_multiplication(add_matrices(c, d), e)
    p4 = strassen_multiplication(d, subtract_matrices(g, e))
    p5 = strassen_multiplication(add_matrices(a, d), add_matrices(e, h))
    p6 = strassen_multiplication(subtract_matrices(b, d), add_matrices(g, h))
    p7 = strassen_multiplication(subtract_matrices(a, c), add_matrices(e, f))

    # Compute result matrices
    c11 = subtract_matrices(add_matrices(add_matrices(p5, p4), p6), p2)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = subtract_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)

    # Merge result matrices
    result = merge_matrices(c11, c12, c21, c22)

    return result


## Example usage and time complexity measurement
input_size = 50  # Change the input size as needed
matrix1 = [[1] * input_size for _ in range(input_size)]
matrix2 = [[2] * input_size for _ in range(input_size)]

start_time_standard = time.time()
result = standard_multiplication(matrix1, matrix2)
end_time_standard = time.time()
execution_time_standard = end_time_standard - start_time_standard

start_time_strassen = time.time()
result = strassen_multiplication(matrix1, matrix2)
end_time_strassen = time.time()
execution_time_strassen = end_time_strassen - start_time_strassen

print("Input Size (n):", input_size)
print("Standard Multiplication Execution Time:", execution_time_standard, "seconds")
print("Strassen's Multiplication Execution Time:", execution_time_strassen, "seconds")

# Example usage and time complexity measurement
input_size = 100  # Change the input size as needed
matrix1 = [[1] * input_size for _ in range(input_size)]
matrix2 = [[2] * input_size for _ in range(input_size)]

start_time_standard = time.time()
result = standard_multiplication(matrix1, matrix2)
end_time_standard = time.time()
execution_time_standard = end_time_standard - start_time_standard

start_time_strassen = time.time()
result = strassen_multiplication(matrix1, matrix2)
end_time_strassen = time.time()
execution_time_strassen = end_time_strassen - start_time_strassen

print("Input Size (n):", input_size)
print("Standard Multiplication Execution Time:", execution_time_standard, "seconds")
print("Strassen's Multiplication Execution Time:", execution_time_strassen, "seconds")