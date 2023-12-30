# Sub-cubic algorithm for multiplying two square n x n matrices
# An n x n matrix will look like a list of lists (2-D array)
# Example: [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]] - this is 4x4 matrix
# First index signifies row number, second index - column number

def split_quadrants(matrix):
    # helper function to split quadrants of matrix
    mid_row = len(matrix) // 2
    mid_col = len(matrix[0]) // 2
    a = [row[:mid_col] for row in matrix[:mid_row]]
    b = [row[mid_col:] for row in matrix[:mid_row]]
    c = [row[:mid_col] for row in matrix[mid_row:]]
    d = [row[mid_col:] for row in matrix[mid_row:]]

    return a, b, c, d


def add_subtract_matrices(A, B, action):
    # helper function to add or subtract square matrices of same size
    if action == '+':
        return [
            [A[i][j] + B[i][j] for j in range(len(A[i]))]
            for i in range(len(A))
        ]
    elif action == "-":
        return [
            [A[i][j] - B[i][j] for j in range(len(A[i]))]
            for i in range(len(A))
        ]


def strassen(matrix_x, matrix_y):
    # separate the sub-matrices, they will have the same dimensions since matrix_x is nxn and matrix_y is nxn
    if len(matrix_x) == 1 and len(matrix_y) == 1:
        return matrix_x[0][0] * matrix_y[0][0]
    a, b, c, d = split_quadrants(matrix_x)
    e, f, g, h = split_quadrants(matrix_y)
    P1 = strassen(a, add_subtract_matrices(f, h, '-'))  # A * (F - H)
    P2 = strassen(add_subtract_matrices(a, b, '+'), h)  # (A + B) * H
    P3 = strassen(add_subtract_matrices(c, d, '+'), e)  # (C + D) * E
    P4 = strassen(d, add_subtract_matrices(g, e, '-'))  # D * (G - E)
    P5 = strassen(add_subtract_matrices(a, d, '+'), add_subtract_matrices(e, h, '+'))  # (A + D) * (E + H)
    P6 = strassen(add_subtract_matrices(b, d, '-'), add_subtract_matrices(g, h, '+'))  # (B - D) * (G + H)
    P7 = strassen(add_subtract_matrices(a, c, '-'), add_subtract_matrices(e, f, '+'))  # (A - C) * (E + F)

    q11 = add_subtract_matrices(add_subtract_matrices(add_subtract_matrices(P5, P4, '+'), P2, '-'), P6,
                                '+')  # P5 + P4 - P2 + P6
    q12 = add_subtract_matrices(P1, P2, '+')  # P1 + P2
    q21 = add_subtract_matrices(P3, P4, '+')  # P3 + P4
    q22 = add_subtract_matrices(add_subtract_matrices(add_subtract_matrices(P1, P5, '+'), P3, '-'), P7,
                                '-')  # P1 + P5 - P3 - P7

    return [q11, q12, q21, q22]


if __name__ == '__main__':
    print(strassen([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
