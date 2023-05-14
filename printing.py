import sys

def print_matrix(matrix):
    for row in matrix:
        print(row)

def clear_console():
    sys.stdout.write("\033[H\033[J")

def pause():
    input("\nPress enter to continue...")