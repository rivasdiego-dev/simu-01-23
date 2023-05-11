import importlib

module_number = input("Enter the number of the node's list to import: ")
nodeListModule = importlib.import_module(f'coordinates.nodes-{module_number}', package='.')


nodeList = nodeListModule.nodeList

print(nodeList)