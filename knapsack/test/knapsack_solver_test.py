import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from knapsack import solver

with open('knapsack/data/ks_4_0', 'r') as input_data_file:
    input_data = input_data_file.read()

def test_solver():
    result = solver.solve_it(input_data)
    assert(result == '18 0\n1 1 0 0')
