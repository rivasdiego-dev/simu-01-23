from datetime import datetime

timestamp = datetime.now().strftime('-%Y-%m-%d--%H-%M-%S')

nodes = int(input('How many nodes you have? '))
filename = input('File number: ')

with open(f'./bin/data/nodeList-{filename}.js', 'w') as f:
    f.write('const nodeList = new Array();\n\n')
    for i in range(nodes):
        f.write('nodeList.push({')
        x = input(f'Enter x coordinate for node {i+1}: ')
        f.write(f'\n    x: "{x}",')
        y = input(f'Enter y coordinate for node {i+1}: ')
        f.write(f'\n    y: "{y}",')
        f.write('\n});\n')
    f.write('\n\nexport default nodeList')