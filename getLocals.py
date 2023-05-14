from matrices import *

def get_jacobian(node1, node2, node3):
    return (
        (node2["x"] - node1["x"]) * (node3["y"] - node1["y"]) -
        (node3["x"] - node1["x"]) * (node2["y"] - node1["y"])
    )

def get_local_k(K, node1, node2, node3):
    localK = 0
    jacobian = get_jacobian(node1, node2, node3)

    product = (K * (jacobian / 2)) / (jacobian * jacobian)
    product = round(product,2)

    localK = multiply_constant_by_matrix(
        product,
        matrix_product(node1, node2, node3)
    )

    return localK

def get_local_b(Q, node1, node2, node3):
    jacobian = get_jacobian(node1, node2, node3)
    product = (Q * jacobian) / 6
    aux_matrix = [[1], [1], [1]]
    localB = multiply_constant_by_matrix(round(product,2), aux_matrix)

    return localB