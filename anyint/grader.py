import re

def grade(input_data, quality_data, submission):
    score = 0.0
    feedback = ''

    subLines = submission.split('\n')

    #print(submission)
    #print(subLines)
    if(len(subLines) < 2) :
        return {'score':0.0, 'feedback':'output should have 1 lines, this one has '+str(len(subLines)-1)}

    try:
        value = int(subLines[0].strip())
    except (ValueError, TypeError):
        return {'score':0.0, 'feedback':'the first output line should only contain one integer, this output has the following bad value: '+subLines[0].strip()}

    try:
        runtime = float(subLines[1])
    except (ValueError, TypeError):
        return {'score': 0,'feedback': 'The evaluation script has failed with error code (2).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}


    if value < 0:
        return {'score':0.0, 'feedback':'the integer you submitted '+str(value)+' does not meet the requirement of being a positive number.'}


    if(value >= quality_data.pt10):
        return {'score':1.0, 'feedback':'Awesome job, the value of '+str(value)+' is sufficient for full credit! '+feedback}
    elif(value >= quality_data.pt3):
        return {'score':0.7, 'feedback':'Your submission output is correct, but the value of '+str(value)+' is insufficient for full credit. For a higher grade, you will need to submit an integer of size '+str(quality_data.pt10)+' or larger. '+feedback}
    else:
        return {'score':0.3, 'feedback':'Your submission output is correct, but the value of '+str(value)+' is insufficient for full credit. For a higher grade, you will need to submit an integer of size '+str(quality_data.pt3)+' or larger. '+feedback}

    return {'score':0.0, 'feedback': 'The evaluation script has failed with error code (1).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}


