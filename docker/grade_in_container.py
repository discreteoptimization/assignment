#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from subprocess import Popen, PIPE

verbose = False

for cmd_line_arg in sys.argv:
    if cmd_line_arg.startswith('-verbose'):
        verbose = True

for dirname, dirnames, filenames in os.walk('..'):
        for filename in filenames:
            if filename.strip() == 'submission.sub':
                file_location = dirname+'/'+filename
                part_id = dirname.split('_')[1]

                print(' '.join(['grading:', part_id, file_location]))
                
                test_cmd = ['courseraprogramming', 'grade', 'local', 'coursera_do_grader',  dirname, 'partId', part_id]
                test_process = Popen(test_cmd, stdout=PIPE, stderr=PIPE, shell=(os.name == 'nt'))
                test_stdout, test_stderr = test_process.communicate()
                if verbose:
                    print(test_stdout)
                    print(test_stderr)
                    print('')
                else:
                    lines = test_stdout.split('\n')
                    active = False
                    for line in lines:
                        if 'Grader output:' in line:
                            active = True
                        if active:
                            print(line)
