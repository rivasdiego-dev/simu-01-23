import importlib
from printing import *
from getLocals import *

# Dynamic import
module_number = input("Enter the number of the node's list to import: ")
nodeListModule = importlib.import_module(f'coordinates.nodes-{module_number}', package='.')

# VARS declaration
nodeList = nodeListModule.nodeList
globalK = 0
globalQ = 0
localBs = []
localKs = []
connectivity_table = []

# FUNC declaration 
def display_menu():
    clear_console()
    print("\nMenu:")
    print("1. Get locals from one element")
    print("2. Get locals from N elements")
    print("3. Fill connectivity table")
    print("4. Print connectivity table")
    print("5. Quit")

def fill_table():
    elements = int(input("How many elements do you have? "))
    print("\n\tFilling the connectivity table")
    for e in range(elements):
        print("\nFor element {0}".format(e+1))
        node1 = int(input("Enter local node 1: "))
        node2 = int(input("Enter local node 2: "))
        node3 = int(input("Enter local node 3: "))
        connectivity_table.append([node1, node2, node3])
    print_table()

def print_table():
    if connectivity_table == []:
        print("\nConnectivity table is empty...\n")
        pause()
        return
    print("\n\tFinal connectivity table\n")
    print_matrix(connectivity_table)
    pause()

def one_element():
    if connectivity_table != []:
        use_one_from_table = input("Do you want to use one from the connectivity table? (y/n) ")
        if use_one_from_table == 'y':
            print_table()
            element_index = int(input("Which element do you want to use? ")) - 1
            node1, node2, node3 = connectivity_table[element_index]
        else:
            node1 = int(input("Enter local node 1: "))
            node2 = int(input("Enter local node 2: "))
            node3 = int(input("Enter local node 3: "))
    else:
        node1 = int(input("Enter local node 1: "))
        node2 = int(input("Enter local node 2: "))
        node3 = int(input("Enter local node 3: "))
            
    print("\n\tLocal K:\n")
    print_matrix(get_local_k(globalK, nodeList[node1-1], nodeList[node2-1], nodeList[node3-1]))
    print("\n\tLocal B:\n")
    print_matrix(get_local_b(globalQ, nodeList[node1-1], nodeList[node2-1], nodeList[node3-1]))
    
def all_elements():
    if connectivity_table == []:
        print("\nConnectivity table is empty...\n")
        pause()
        return
    
    
    
# Main workflow

globalK = float(input("Please, enter the global K value: "))
globalQ = float(input("Please, enter the global Q value: "))

display_menu()
while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        one_element()
        
    elif choice == "2":
        all_elements()
        
    elif choice == "3":
        fill_table()
        
    elif choice == "4":
        print_table()
        
    elif choice == "5":
        print("\nClosing program...")
        break  
    else:
        print("Invalid choice. Please try again.")
    display_menu()