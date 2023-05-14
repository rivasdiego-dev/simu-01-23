from getLocals import *

def assemble_global_k(nodeList, assembled_local_Ks, connectivity_table):
    global_K = [[0 for _ in range(len(nodeList))] for _ in range(len(nodeList))]
    
    for i in range(len(nodeList)):
        for j in range(len(nodeList)):
            print
    
    return global_K

def assemble_global_b(nodeList, assembled_local_Bs , connectivity_table):
    global_B = [[0] for _ in range(len(nodeList))]

    for i in range(len(nodeList)):
        for j in range(len(nodeList)):
            print

    return global_B