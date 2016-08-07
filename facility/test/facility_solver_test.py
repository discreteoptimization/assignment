import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from facility import solver

with open('facility/data/fl_3_1', 'r') as input_data_file:
    input_data = input_data_file.read()

def test_solver():
    result = solver.solve_it(input_data)
    assert(result == '2545.77 0\n0 0 1 2')

