def grade(input_data, quality_data, submission):
    score = 0
    scoreUB = 1
    feedback = ''

    lines = input_data.split('\n')

    firstLine = lines[0].split();
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    edges = []
    #print(firstLine)
    for i in range(1,edgeCount+1):
        line = lines[i]
        parts = line.split()
        #print(parts)
        edges.append((int(parts[0]), int(parts[1])))

    subLines = submission.splitlines();
    if(len(subLines) != 3) :
        return {'score':0.0, 'feedback':'output should have 2 lines, this one has '+str(len(subLines)-1)}

    lineOneParts = subLines[0].split()
    if(len(lineOneParts) != 2) :
        return {'score':0.0, 'feedback':'the first output line should have 2 values, this one has '+str(len(lineOneParts))}

    try:
        obj = int(lineOneParts[0])
    except (ValueError, TypeError):
       return {'score':0.0, 'feedback':'the first output line should only contain numbers, this output has the following bad value: '+lineOneParts[0]}
    obj = int(obj)

    try:
        opt = int(lineOneParts[1])
    except (ValueError, TypeError):
        return {'score':0.0, 'feedback':'the first output line should only contain numbers, this output has the following bad value: '+lineOneParts[1]}


    lineTwoParts = subLines[1].split()
    if(len(lineTwoParts) != nodeCount) :
        return {'score':0.0, 'feedback':'the second output line should have '+str(nodeCount)+' values, this one has '+str(len(lineTwoParts))}
    #print lineTwoParts

    badVals = set()
    for v in lineTwoParts:
        if not v.isdigit():
            badVals.add(v)
    if len(badVals) > 0:
        return {'score':0.0, 'feedback':'the second output line should only contain integers, this output has the following bad values: '+(', '.join(map(str,badVals)))}

    lineTwoParts = [int(x) for x in lineTwoParts]
    try:
        runtime = float(subLines[2])
    except (ValueError, TypeError):
        return {'score':0.0, 'feedback': 'The evaluation script has failed with error code (2).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}

    colors = lineTwoParts

    colorViolations = ''
    for edge in edges:
        if(colors[edge[0]] == colors[edge[1]]):
            colorViolations = colorViolations+'('+str(edge[0])+','+str(edge[1])+') ';
    if(len(colorViolations) > 1):
        return {'score':0.0, 'feedback':'the different color constraint was not satisfied on the following edges: '+colorViolations}

    value = len(set(colors))
    if value != obj :
        feedback = feedback + '\nWarning: submitted objective value is inconsistent with actual value. given: '+str(obj)+' actual value: '+str(value)

    #if opt :
    #    results = db.checkForLess(metadata.assignment_id, problem_id, value)
    #    if results != None and len(results) > 0 :
    #        bestVal = min(map(lambda x: x[4], results)) #4 is the quality column in the DB
    #        feedback = feedback + '\nWarning: your algorithm claimed to have an optimal solution with objective value '+str(value)+'.  However, a solution exists with an objective value of '+str(int(bestVal))+' demonstrating that your solution is not optimal.'

    if(runtime > 18000.0) :
        feedback = feedback + '\nNote: your algorithm runtime exceeded the time limit (5 hours), setting your score limit to 7.  For a better grade, run your algorithm within the 5 hour time limit.'
        scoreUB = 0.7


    if(value <= quality_data.pt10):
        if opt:
            return {'score':min(1.0, scoreUB), 'feedback':'Awesome Optimization! Your algorithm is competitive with an expert solution and your solution objective value '+str(value)+' appears to be optimal!  You can\'t beat that.'+feedback}
        else :
            return {'score':min(1.0, scoreUB), 'feedback':'Awesome Optimization! Your algorithm is competitive with an expert solution. Can you prove that your solution objective value '+str(value)+' is optimal? '+feedback}
    elif(value <= quality_data.pt3):
        return {'score':min(0.7, scoreUB), 'feedback':'Good Optimization. Your algorithm does some basic optimization but your solution objective value '+str(value)+' can be improved significantly. For a higher grade, you will need to improve the objective value to '+str(quality_data.pt10)+' or better. '+feedback}
    else:
        return {'score':min(0.3, scoreUB), 'feedback':'Your submission output is good, but the solution objective value '+str(value)+' is insufficient for full credit. For a higher grade, you will need to improve the objective value to '+str(quality_data.pt3)+' or better. '+feedback}

    return {'score':0.0, 'feedback': 'The evaluation script has failed with error code (1).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}


