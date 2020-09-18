#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

# Create array for Items and add index, value and weight to array
    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

# Create tuple for paths for solution
    names = "x1"
    for i in range(1, item_count):
        names = names + ", x" + str(i+1)
    Path = namedtuple("Paths", names)
    paths = []
    for i in range (0,2 ** item_count):
        path = f"{i:b}".zfill(len(f"{(2 ** item_count) - 1:b}"))
        paths.append(Path(int(path[0]), int(path[1]), int(path[2]), int(path[3])))
## ??Works for 4 columns tuple - how do I do this for n column tuple??

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    #value = 0
    #weight = 0
    #taken = [0]*len(items)

    #for item in items:
    #    if weight + item.weight <= capacity:
    #        taken[item.index] = 1
    #        value += item.value
    #        weight += item.weight
    
    # In here will write the code for Branch and Bound routine #
    
    # prepare the solution in the specified output format
    #output_data = str(value) + ' ' + str(0) + '\n'
    #output_data += ' '.join(map(str, taken))
    #return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

