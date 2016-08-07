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
