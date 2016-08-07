import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from screenname import grader

input_data = ''
quality = PartQuality('test', 0, 0)

# Score Test
def test_full_credit_one():
    result = grader.grade(input_data, quality, 'MyBestName\n123\n')
    print(result['feedback'])
    assert(result['score'] == 1.0)

def test_full_credit_two():
    result = grader.grade(input_data, quality, 'MyBestName')
    assert(result['score'] == 1.0)

def test_full_credit_three():
    result = grader.grade(input_data, quality, u'abc \u2220 def\n123\n')
    assert(result['score'] == 0.0)

def test_full_credit_long_one():
    result = grader.grade(input_data, quality, '123456789 123456789 123456789 123456790\n123\n')
    assert(result['score'] == 1.0)

def test_full_credit_long_two():
    result = grader.grade(input_data, quality, '123456789_123456789_123456789_123456790\n123\n')
    assert(result['score'] == 1.0)

def test_full_credit_long_three():
    result = grader.grade(input_data, quality, '123456789_123456789_0\n123\n')
    assert(result['score'] == 1.0)

def test_full_credit_long_four():
    result = grader.grade(input_data, quality, '123456789_123456789_\n123\n')
    assert(result['score'] == 1.0)


# Constraint Tests
def test_empty_string():
    result = grader.grade(input_data, quality, '\n123\n')
    assert(result['score'] == 0.0)

def test_too_long():
    result = grader.grade(input_data, quality, '1234567890 1234567890 1234567890 1234567890\n123\n')
    assert(result['score'] == 0.0)

def test_invalid_char_one():
    result = grader.grade(input_data, quality, 'abc % \def\n123\n')
    assert(result['score'] == 0.0)

def test_invalid_char_two():
    result = grader.grade(input_data, quality, 'abc \n def\n123\n')
    assert(result['score'] == 0.0)
