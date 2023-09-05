#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve_it(input_data):
    # return a positive integer, as a string

    # TODO replace with call to your solver
    return trivial_solver(0)


def parse_input(_):
    pass


def trivial_solver(n):
    # a trivial algorithm returning a number
    if n is None:
        n = 0
    return str(n)


if __name__ == '__main__':
    print('This script submits the integer: %s\n' % solve_it(''))

