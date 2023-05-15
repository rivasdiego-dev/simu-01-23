import sys

def print_matrix(matrix):
    for row in matrix:
        formatted_row = ["{:>7.2f}".format(element) for element in row]
        print(" ".join(formatted_row))

def print_locals(locals):
    for i, matrix in enumerate(locals, start=1):
        print(f"Local {i}:")
        print_matrix(matrix)
        print()