#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    edges, node_count, edge_count = parse_input(input_data)

    # TODO replace with your solver
    solution = trivial_solver(edges, node_count, edge_count)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


def parse_input(input_data):
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    return edges, node_count, edge_count


def trivial_solver(_edges, node_count, _edge_count):
    # a trivial solution, every node has its own color
    solution = range(0, node_count)

    return solution


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

