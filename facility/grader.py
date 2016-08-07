import math
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
Facility = namedtuple("Facility", ['index', 'setup_cost', 'capacity', 'location'])
Customer = namedtuple("Customer", ['index', 'demand', 'location'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def grade(input_data, quality_data, submission):
    score = 0
    scoreUB = 1.0
    feedback = ''

    lines = input_data.split('\n')

    parts = lines[0].split()
    facility_count = int(parts[0])
    customer_count = int(parts[1])
    
    facilities = []
    for i in range(1, facility_count+1):
        parts = lines[i].split()
        facilities.append(Facility(i-1, float(parts[0]), int(parts[1]), Point(float(parts[2]), float(parts[3])) ))

    customers = []
    for i in range(facility_count+1, facility_count+1+customer_count):
        parts = lines[i].split()
        customers.append(Customer(i-1-facility_count, int(parts[0]), Point(float(parts[1]), float(parts[2]))))
    
    
    subLines = submission.splitlines();
    if(len(subLines) != 3) :
        return {'score':0.0, 'feedback':'output should have 2 lines, this one has '+str(len(subLines)-1)}

    lineOneParts = subLines[0].split()
    if(len(lineOneParts) != 2) :
        return {'score':0.0, 'feedback':'the first output line should have 2 values, this one has '+str(len(lineOneParts))}

    try:
        obj = int(float(lineOneParts[0]))
    except:
        return {'score':0.0, 'feedback':'the first output line should only contain numbers, this output has the following bad value: '+lineOneParts[0]}

    try:
        opt = int(lineOneParts[1])
    except:
        return {'score':0.0, 'feedback':'the first output line should only contain numbers, this output has the following bad value: '+lineOneParts[1]}

    lineTwoParts = subLines[1].split()
    if(len(lineTwoParts) != customer_count) :
        return {'score':0.0, 'feedback':'the second output line should have '+str(customer_count)+' values, this one has '+str(len(lineTwoParts))}

    badVals = set()
    for v in lineTwoParts:
        if not v.isdigit():
            badVals.add(v)
    if len(badVals) > 0:
        return {'score':0.0, 'feedback':'the second output line should only contain integers, this output has the following bad values: '+(', '.join(map(str,badVals)))}

    lineTwoParts = [int(x) for x in lineTwoParts]
    badVals = set()
    for v in lineTwoParts:
        if v < 0 or v > facility_count-1:
            badVals.add(v)
    if len(badVals) > 0:
        return {'score':0.0, 'feedback':'the second output line should only contain values between 0 and '+str(facility_count-1)+', this output has the following bad values: '+(', '.join(map(str,badVals)))}

    try:
        runtime = float(subLines[2])
    except (ValueError, TypeError):
        return {'score':0.0, 'feedback': 'The evaluation script has failed with error code (2).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}
    
    assignment = lineTwoParts

    load = [0]*facility_count

    for c in range(0,customer_count):
        load[assignment[c]] += customers[c].demand

    overloaded = []
    for f in range(0,facility_count):
        if load[f] > facilities[f].capacity:
            overloaded.append('facility '+str(f)+' is over the capacity limit by '+str(load[f]-facilities[f].capacity))
    if len(overloaded) > 0:
       return {'score':0.0, 'feedback':'the solution has facility capacity violations: '+', '.join(overloaded)}


    value = sum(map(lambda f: 0 if load[f]==0 else facilities[f].setup_cost, range(0,facility_count)))
    for c in range(0, customer_count):
        value += length(customers[c].location, facilities[assignment[c]].location)

    #print obj, value
    if abs(value - obj) > 1.0 :
        feedback = feedback + '\nWarning: submitted objective value is inconsistent with actual value. given: '+str(obj)+' actual value: '+str(value)

    # if opt :
    #     results = db.checkForLess(metadata.assignment_id, problem_id, value)
    #     if results != None and len(results) > 0: # todo we should make this a little mode robust to floating point arithmetic
    #         bestVal = min(map(lambda x: x[4], results)) #4 is the quality column in the DB
    #         feedback = feedback + '\nWarning: your algorithm claimed to have an optimal solution with objective value '+str(value)+'.  However, a solution exists with an objective value of '+str(int(bestVal))+' demonstrating that your solution is not optimal.'

    if(runtime > 18000.0) :
        feedback = feedback + '\nNote: your algorithm runtime exceeded the time limit (5 hours), setting your score limit to 7.  For a better grade, run your algorithm within the 5 hour time limit.'
        scoreUB = 0.7

    if(value <= quality_data.pt10):
        if opt:
            return {'score':min(1.0,scoreUB), 'feedback':'Awesome Optimization! Your algorithm is competitive with an expert solution and your solution objective value '+str(value)+' appears to be optimal!  You can\'t beat that.'+feedback}
        else :
            return {'score':min(1.0,scoreUB), 'feedback':'Awesome Optimization! Your algorithm is competitive with an expert solution. Can you prove that your solution objective value '+str(value)+' is optimal? '+feedback}
    elif(value <= quality_data.pt3):
        return {'score':min(0.7,scoreUB), 'feedback':'Good Optimization. Your algorithm does some basic optimization but your solution objective value '+str(value)+' can be improved significantly. For a higher grade, you will need to improve the objective value to '+str(quality_data.pt10)+' or better. '+feedback}
    else:
        return {'score':min(0.3,scoreUB), 'feedback':'Your submission output is good, but the solution objective value '+str(value)+' is insufficient for full credit. For a higher grade, you will need to improve the objective value to '+str(quality_data.pt3)+' or better. '+feedback}

    return {'score':0.0, 'feedback': 'The evaluation script has failed with error code (1).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}

