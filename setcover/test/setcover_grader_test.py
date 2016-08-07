import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from setcover import grader

with open('setcover/data/sc_6_1', 'r') as input_data_file:
    input_data = input_data_file.read()

quality = PartQuality('test', 3, 2)

greedy_submission = '3.0 0\n0 1 0 1 1 0\n123\n'
opt_submission    = '2.0 0\n0 0 0 0 1 1\n123\n'


# Score Test
def test_full_credit():
    result = grader.grade(input_data, quality, opt_submission)
    assert(result['score'] == 1.0)

def test_full_credit_opt():
    result = grader.grade(input_data, quality, '2.0 1\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 1.0)

def test_full_credit_opt_big():
    result = grader.grade(input_data, quality, '2.0 99\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 1.0)

def test_full_credit_opt_neg():
    result = grader.grade(input_data, quality, '2.0 -99\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 1.0)

def test_partial_credit():
    result = grader.grade(input_data, quality, greedy_submission)
    assert(result['score'] == 0.7)

def test_feasible_credit():
    result = grader.grade(input_data, quality, '5.0 0\n1 1 1 1 1 0\n123\n')
    assert(result['score'] == 0.3)

def test_partial_credit_timelimit():
    result = grader.grade(input_data, quality, '2.0 0\n0 0 0 0 1 1\n99999\n')
    assert(result['score'] == 0.7)
    assert('runtime exceeded' in result['feedback'])

def test_objective_value_warning():
    result = grader.grade(input_data, quality, '3.0 0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 1.0)
    assert('Warning' in result['feedback'])

# Not implementable without the leader board
# passed += testGrade(grade, metadata, db, 'Opt Flag Warning (7/10): '  , '3.0 1\n0 1 0 1 1 0\n123\n', 7)


# Constraint Tests
def test_item_cover_violated():
    result = grader.grade(input_data, quality, '1.0 0\n1 0 0 0 0 0\n123\n')
    assert(result['score'] == 0.0)


# I/O Tests
def test_objective_line_long():
    result = grader.grade(input_data, quality, '2.0 0 0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_objective_line_short():
    result = grader.grade(input_data, quality, '0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_solution_line_long():
    result = grader.grade(input_data, quality, '2.0 0\n0 0 0 0 1 1 0\n123\n')
    assert(result['score'] == 0.0)

def test_solution_line_short():
    result = grader.grade(input_data, quality, '2.0 0\n0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_line_count_long():
    result = grader.grade(input_data, quality, '0\n2.0 0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_line_count_short():
    result = grader.grade(input_data, quality, '0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)


# Type Tests
def test_nan_objective():
    result = grader.grade(input_data, quality, 'NaN 0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_inf_objective():
    result = grader.grade(input_data, quality, 'Inf 0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_alpha_objective():
    result = grader.grade(input_data, quality, 'a 0\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_alpha_optflag():
    result = grader.grade(input_data, quality, '2.0 b\n0 0 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_alpha_solution():
    result = grader.grade(input_data, quality, '2.0 0\n0 c 0 0 1 1\n123\n')
    assert(result['score'] == 0.0)

def test_alpha_time():
    result = grader.grade(input_data, quality, '2.0 0\n0 0 0 0 1 1\n123d\n')
    assert(result['score'] == 0.0)

def test_range_solution():
    result = grader.grade(input_data, quality, '2.0 0\n0 0 3 0 2 1\n123\n')
    assert(result['score'] == 0.0)

