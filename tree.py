import argparse

GV_HEADER = '''
digraph tree {
node [color = grey, style = filled];
'''

GV_FOOTER = '''
}
'''

def write_gv(filename, nodes, edges):
    '''Writes nodes, edges to filename in graphviz format'''
    with open(filename, 'w') as file:
        file.write('%s\n' % GV_HEADER)

        for n in nodes:
            file.write('"%s" [color = lightblue];\n' % n)

        for (n1, n2) in edges:
            file.write('"%s" -> "%s"\n' % (n1, n2))

        file.write('%s\n' % GV_FOOTER)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in', '-i', required = True, help = 'Input relations file')
    parser.add_argument('--out', '-o', required = True, help = 'Output graphviz file')
    options = vars(parser.parse_args())

    nodes = []
    edges = []

    with open(options['in']) as file:
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

# Write graphviz output file
write_gv(options['out'], nodes, edges)
print 'Created tree with %d persons' % len(nodes)
