from getLocals import *

def assemble_global_k(nodeList, local_ks, connectivity_table):
    global_K = [[0 for _ in range(len(nodeList))] for _ in range(len(nodeList))]

    
    
    return global_K

def assemble_global_b(nodeList, local_bs , connectivity_table):
    global_B = [[0] for _ in range(len(nodeList))]
    
    for p in range(len(local_bs)):
        for q in range(len(local_bs[0])):
            for r in range(len(local_bs[p][0])):
                global_B[connectivity_table[p][q]-1][r] = round(global_B[connectivity_table[p][q]-1][r] + local_bs[p][q][r], 2)
            
    return global_B

