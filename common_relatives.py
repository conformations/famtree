# Identifies common relatives among a set of 23AndMe relative finder
# csv files. A relative is included in the output if and only if he/she
# is present in all files.

import csv
import sys

def LoadRelatives(filename):
    """Returns the set of names from a 23AndMe relative finder csv."""
    names = set()

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name'].strip()
            if name:
                names.add(name)

    return names

def Intersect(first, second):
    """Returns the intersection of two sets."""
    return first.intersection(second)

if __name__ == '__main__':
    filenames = sys.argv[1:]
    relatives = [LoadRelatives(filename) for filename in filenames]

    # In order to be retained in the output, an individual must be
    # included in the relative finder results for all individuals.
    common_relatives = reduce(Intersect, relatives)
    for (i, relative) in enumerate(common_relatives):
      print '(%d) %s' % (i+1, relative)

