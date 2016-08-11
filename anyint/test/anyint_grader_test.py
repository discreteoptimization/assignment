import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from anyint import grader

input_data = ''
quality = PartQuality('test', 7, 10)

greedy_submission = '7\n123\n'
opt_submission = '10\n123\n'


# Score Test
def test_full_credit():
    result = grader.grade(input_data, quality, opt_submission)
    assert(result['score'] == 1.0)

def test_partial_credit():
    result = grader.grade(input_data, quality, greedy_submission)
    assert(result['score'] == 0.7)

def test_feasible_credit():
    result = grader.grade(input_data, quality, '5\n123\n')
    assert(result['score'] == 0.3)


# Constraint Tests
def test_positivity_violated():
    result = grader.grade(input_data, quality, '-1\n123\n')
    assert(result['score'] == 0.0)
    assert('positive' in result['feedback'])


# I/O Tests
def test_number_line_long():
    result = grader.grade(input_data, quality, '10 0\n123\n')
    assert(result['score'] == 0.0)

def test_number_line_short():
    result = grader.grade(input_data, quality, ' \n123\n')
    assert(result['score'] == 0.0)

def test_line_count_long():
    result = grader.grade(input_data, quality, '0\n 10\n 123\n')
    assert(result['score'] == 0.3)

def test_line_count_short():
    result = grader.grade(input_data, quality, '123\n')
    assert(result['score'] == 0.0)


# Type Tests
def test_nan_number():
    result = grader.grade(input_data, quality, 'NaN\n123\n')
    assert(result['score'] == 0.0)

def test_inf_number():
    result = grader.grade(input_data, quality, 'Inf\n123\n')
    assert(result['score'] == 0.0)

def test_alpha_number():
    result = grader.grade(input_data, quality, 'a\n123\n')
    assert(result['score'] == 0.0)

def test_alpha_time():
    result = grader.grade(input_data, quality, '10\n123d\n')
    assert(result['score'] == 0.0)

def test_float_number():
    result = grader.grade(input_data, quality, '8.7\n123\n')
    assert(result['score'] == 0.0)


