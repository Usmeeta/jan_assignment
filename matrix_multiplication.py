import numpy as np

# Create two 2D arrays 
matrix_a = np.array([[3, 2], [5, 9]])
matrix_b = np.array([[4, 6], [1, 8]])

result = np.dot(matrix_a, matrix_b)


print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nResult of Matrix A * Matrix B:")
print(result)
