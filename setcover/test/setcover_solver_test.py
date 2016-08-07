import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from setcover import solver

with open('setcover/data/sc_6_1', 'r') as input_data_file:
    input_data = input_data_file.read()

def test_solver():
    result = solver.solve_it(input_data)
    assert(result == '5.0 0\n1 1 1 1 1 0')

