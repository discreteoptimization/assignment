import os, pytest

import do_grader


submission_dirs = []

for wd, directory, files in os.walk('.'):
    for file in files:
        if file == 'submission.sub':
            submission_dirs.append(wd.split('/')[-1])
del wd, directory, files

print(submission_dirs)

@pytest.mark.parametrize("submission_dir", submission_dirs)

def test_001(submission_dir):
    do_grader.main(submission_dir.strip('_'), None, None, submission_dir+'/submission.sub')

    # lets be extra strick and flag warnings here as well
    # warnings.filterwarnings('error')

    # case = gcg_mpdata.io.parse_mp_case_file(correct_input_data)
    # mp_data = case.to_matpower()
    # case_2 = gcg_mpdata.io.parse_mp_case_str(mp_data)
    # assert case == case_2 # checks full data structure
    # assert not case != case_2
    # assert str(case) == str(case_2) # checks string representation of data structure

    # # need to set warnings back to default
    # # otherwise tests using pytest.warns will fail
    # warnings.resetwarnings()

def test_default_values():
    argv = ['partId', '1']
    part_id, user_id, orginial_filename, submission_location = do_grader.parse_sys_args(argv)

    assert(part_id == '1')
    assert(user_id == None)
    assert(orginial_filename == None)
    assert(submission_location == '/shared/submission/submission.sub')

def test_non_default_values():
    argv = ['filename', '3', 'override_sub', '4', 'partId', '1', 'userId', '2']

    part_id, user_id, orginial_filename, submission_location = do_grader.parse_sys_args(argv)

    assert(part_id == '1')
    assert(user_id == '2')
    assert(orginial_filename == '3')
    assert(submission_location == '4')


def test_no_values():
    argv = []
    with pytest.raises(SystemExit):
        part_id, user_id, orginial_filename, submission_location = do_grader.parse_sys_args(argv)

def test_no_partid():
    argv = ['filename', '3']
    with pytest.raises(SystemExit):
        part_id, user_id, orginial_filename, submission_location = do_grader.parse_sys_args(argv)
