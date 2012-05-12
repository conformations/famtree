import sys

header = '''
digraph tree {
  size = "8,28"
  node [color = grey, style = filled];
  node [fontname = "Verdana", size = "30,30"];
'''

footer = '''
}
'''

if __name__ == '__main__':
    filename = sys.argv[1]

    nodes = []
    edges = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # Format: offspring : parent1, parent2
            cols = line.split(':')

            offspring = cols[0].strip()
            parents = [e.strip() for e in cols[1].split(',')]

            nodes.append(offspring)
            [edges.append((p, offspring)) for p in parents]


with open('tree.gv', 'w') as file:
    file.write('%s\n' % header)

    for n in nodes:
        file.write('"%s" [color = lightblue];\n' % n)
    for (n1, n2) in edges:
        file.write('"%s" -> "%s"\n' % (n1, n2))

    file.write('%s\n' % footer)
