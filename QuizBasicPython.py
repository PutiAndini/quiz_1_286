class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        flatten_matrix = [item for sublist in self.matrix for item in sublist]
        return min(flatten_matrix), max(flatten_matrix)

    def transpose_matrix(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

    def multiply_matrices(self, other_matrix):
        result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other_matrix)] for row_a in self.matrix]
        return result

    def add_matrices(self, other_matrix):
        result = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.matrix, other_matrix)]
        return result


if __name__ == "__main__":
    matrix_a = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_operations = MatrixOperations(matrix_a)

    min_value, max_value = matrix_operations.find_min_max()
    print(f"Min value: {min_value}")
    print(f"Max value: {max_value}")

    transposed_matrix = matrix_operations.transpose_matrix()
    print("Transposed Matrix:")
    for row in transposed_matrix:
        print(row)

    result_multiply = matrix_operations.multiply_matrices(transposed_matrix)
    print("Result of Matrix Multiplication:")
    for row in result_multiply:
        print(row)

    result_addition = matrix_operations.add_matrices(transposed_matrix)
    print("Result of Matrix Addition:")
    for row in result_addition:
        print(row)
