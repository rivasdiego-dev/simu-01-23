def transpose_matrix(M):
    rows = len(M)
    cols = len(M[0])

    # Create a new matrix to store the transposed values
    result = [[None] * rows for _ in range(cols)]

    # Populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            result[j][i] = M[i][j]

    return result

def multiply_constant_by_matrix(k, M):
    result = []

    # Multiply each element in the matrix by the constant
    for i in range(len(M)):
        row = []
        for j in range(len(M[i])):
            row.append(round(k * M[i][j],2))
        result.append(row)

    return result

def multiply_matrices(m1, m2):
    result = []

    for i in range(len(m1)):
        result.append([])
        for j in range(len(m2[0])):
            sum = 0
            for k in range(len(m1[0])):
                sum += m1[i][k] * m2[k][j]
            result[i].append(round(sum,2))

    return result

def matrix_product(node1, node2, node3):
    A = [
        [node3["y"] - node1["y"], node1["x"] - node3["x"]],
        [node1["y"] - node2["y"], node2["x"] - node1["x"]]
    ];
    B = [
        [-1, 1, 0],
        [-1, 0, 1]
    ]
    AT = transpose_matrix(A)
    BT = transpose_matrix(B)

    BTAT = multiply_matrices(BT, AT)
    BTATA = multiply_matrices(BTAT, A)
    result = multiply_matrices(BTATA, B)

    return result

