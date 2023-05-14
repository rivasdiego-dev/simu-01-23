nodes = int(input('How many nodes you have? '))
filename = input('File number: ')

with open(f'./coordinates/nodes-{filename}.py', 'w') as f:
    f.write('nodeList = [\n')
    for i in range(nodes):
        x = input(f'Enter x coordinate for node {i+1}: ')
        y = input(f'Enter y coordinate for node {i+1}: ')
        f.write('{{"x": {0}, "y": {1}}},\n'.format(x, y))
    f.write(']')
print(f"\nNew node list created!\nUnder dir ./coordinates\n\tFile name: nodes-{filename}.py")
