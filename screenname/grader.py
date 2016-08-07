import re

def grade(input_data, quality_data, submission):
    score = 0.0
    feedback = ''

    lines = submission.split('\n')

    if(len(lines) > 3) :
        return {'score':0.0, 'feedback':'output should have no more than 2 lines, this one has '+str(len(lines)-1)}

    first_line = lines[0].strip()
    if len(first_line) <= 0:
        return {'score':0.0, 'feedback':'empty screen name submitted'}

    if len(first_line) > 40:
        return {'score':0.0, 'feedback':'the submitted screen name was too long. Submitted name was '+str(len(first_line))+' characters long but only 40 characters or less are permitted. Try submitting a shorter screen name.'}

    #try:
    #    first_line = first_line.decode('ascii')
    #except UnicodeDecodeError:
    #    return {'score':0.0, 'feedback':'the submitted screen name contains non-ASCII characters. Only ASCII characters are allowed. Try submitting a different screen name.'}

    if not re.match(r'^[ \w-]+$', first_line):
        return {'score':0.0, 'feedback':'the submitted screen name \''+first_line+'\' contains invalid characters. Only alpha numerical characters, dashes, and underscores are allowed. Try submitting a different screen name.'}

    return {'score':1.0, 'feedback':'Congratulations! Your screen name has been set to '+first_line+'.'+feedback}


