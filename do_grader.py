#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys, os

from do_grader_lib import GraderMetadata
from do_grader_lib import Part
from do_grader_lib import PartQuality


def print_stderr(*args):
    sys.stderr.write(' '.join(map(str,args))+'\n')

def load_grader_meta_data(directory=''):
    part_data = {}
    
    try:
        with open(directory+'_coursera', 'r') as metadata_file:
            url = metadata_file.readline().strip()
            name = metadata_file.readline().strip()
            for line in metadata_file.readlines():
                if ',' in line:
                    line_parts = line.split(',')
                    line_parts = [x.strip() for x in line_parts]
                    assert(len(line_parts) == 4)
                    part = Part(*line_parts)
                    part_data[part.id] = part
    except Exception as e:
        print('problem parsing assignment metadata file')
        print('exception message:')
        print(e)
        quit()

    try:
        with open(directory+'_metadata_grader', 'r') as grader_metadata_file:
            sense = int(grader_metadata_file.readline().strip())
            
            quality_data = {}
            for line in grader_metadata_file.readlines():
                line_parts = line.split(',')
                line_parts = [x.strip() for x in line_parts]
                assert(len(line_parts) == 3)
                line_parts[1] = int(line_parts[1])
                line_parts[2] = int(line_parts[2])
                quality = PartQuality(*line_parts)
                quality_data[quality.id] = quality

    except Exception as e:
        print('problem parsing grader metadata file')
        print('exception message:')
        print(e)
        quit()
    
    assert(len(part_data) == len(quality_data));
    
    return GraderMetadata(url, name, sense, part_data, quality_data)


def post(result):
    score = result['score']
    feedback = result['feedback'].replace('\n','\\n')  # escape line breaks so coursera accepts the grading string
    print('{"fractionalScore": %f, "feedback": "%s"}' % (score, feedback))


def start_grader(metadata, part_id, user_id, orginial_filename, submission_location):
    print_stderr('User ID:  ', user_id)
    print_stderr('Part ID:  ', part_id)
    print_stderr('Filename: ', orginial_filename)
    print_stderr('Sub. Loc.:', submission_location)
    
    print_stderr('\nRunning '+metadata.name+' Grader')
    print_stderr('')

    try:
        #TODO make sure this is of the form name.py, no relative path
        pkg = __import__('grader')
        if not hasattr(pkg, 'grade'):
            print('the grade() function was not found in grader')
            quit()
    except ImportError as e:
        print('grader was not found in current working directory.')
        print(str(e))
        quit()

    with open(submission_location, 'r') as submission_file:
        submission = submission_file.read()

    input_file = metadata.part_data[part_id].input_file
    quality_data = metadata.quality_data[part_id]
    
    print_stderr('Input File: %s' % input_file)
    print_stderr('Student Submission:\n%s' % submission)

    with open(input_file, 'r') as input_data_file:
        input_data = input_data_file.read()

    result = pkg.grade(input_data, quality_data, submission)
    post(result)

    # undo module import so that multiple grades can be done during testing
    del sys.modules['grader']


def load_metadata_lookup():
    metadata_lookup = {}
    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            #print(filename
            if filename.strip() == '_metadata_grader':
                metadata_location = dirname+'/'+filename

                try:
                    metadata = load_grader_meta_data(dirname+'/')

                except Exception as e:
                    print_stderr('FAILED to read metadata files for '+dirname+'(skipped) !!!!')
                    print_stderr(e)
                    #print_stderr(traceback.format_exc())
                    continue

                #print_stderr(dirname)
                #print_stderr(metadata)
                metadata_items = [dirname, metadata]

                for part_data_id in metadata.part_data.keys():
                    metadata_lookup[part_data_id] = metadata_items

    return metadata_lookup


def main(part_id, user_id, orginial_filename, submission_location):
    metadata_lookup = load_metadata_lookup()

    if not part_id in metadata_lookup.keys():
        print_stderr('part id not found in metadata lookup!!!!')
        quit()

    #print_stderr(os.getcwd())
    dirname, metadata = metadata_lookup[part_id]
    

    os.chdir(dirname)
    # add so grader can be imported
    sys.path.append(os.getcwd())
    
    start_grader(metadata, part_id, user_id, orginial_filename, submission_location)

    # undo cwd and path, so that multiple grades can be done during testing
    sys.path.pop()
    os.chdir('..')


def parse_sys_args(argv):
    print(argv)
    part_id = None
    user_id = None
    orginial_filename = None
    submission_location = '/shared/submission/submission.sub'

    #print(argv)
    if len(argv) <= 1:
        print_stderr('no command line arguments given!!!!')
        quit()

    for i in range(len(argv)):
        if 'partId' in argv[i] and i+1 < len(argv):
            part_id = argv[i+1]
        if 'userId' in argv[i] and i+1 < len(argv):
            user_id = argv[i+1]
        if 'filename' in argv[i] and i+1 < len(argv):
            orginial_filename = argv[i+1]
        if 'override_sub' in argv[i] and i+1 < len(argv):
            submission_location = argv[i+1]

    if part_id is None:
        print_stderr('no part id found!!!!')
        quit()

    return part_id, user_id, orginial_filename, submission_location


if __name__ == '__main__':
    main(*parse_sys_args(sys.argv))



    