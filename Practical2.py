# Practical 2: Implementation of Array applications of Sparse Matrices.  
#  Name: Shivam Maisuriya
#  Enrollment No: 202203103510303
# Batch:B.Tech CSE

def transpose_sparse_matrix(matrix):
    transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_sparse_matrices(matrix1, matrix2):
    result_matrix = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix

def multiply_matrices(matrix1, matrix2):
    result_matrix = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix

# Example sparse matrix
sparse_matrix = [
    [1, 0, 1],
    [0, 2, 0],
    [0, 0, 3]
]
print("Original Sparse Matrix ")
print_matrix(sparse_matrix)

print("\nTransposed Sparse Matrix ")
transposed_matrix = transpose_sparse_matrix(sparse_matrix)
print_matrix(transposed_matrix)

print("\nAddition of Sparse Matrix and Transposed Matrix")
add_matrix = add_sparse_matrices(sparse_matrix, transposed_matrix)
print_matrix(add_matrix)

print("\nMultiplication of Sparse Matrix and Transposed Matrix")
multiply_matrix = multiply_matrices(sparse_matrix, transposed_matrix)
print_matrix(multiply_matrix)

