import sys

def print_matrix(matrix):
    for row in matrix:
        print(row)

def print_locals(locals):
    for i, matrix in enumerate(locals, start=1):
        print(f"Local {i}:")
        for row in matrix:
            print(row)
        print()