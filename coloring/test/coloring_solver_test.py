import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from coloring import solver

with open('coloring/data/gc_4_1', 'r') as input_data_file:
    input_data = input_data_file.read()

def test_solver():
    result = solver.solve_it(input_data)
    assert(result == '4 0\n0 1 2 3')

