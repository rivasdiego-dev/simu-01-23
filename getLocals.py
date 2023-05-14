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
