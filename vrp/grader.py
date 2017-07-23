import math
from collections import namedtuple

Customer = namedtuple("Customer", ['index', 'demand', 'x', 'y'])

def length(customer1, customer2):
    return math.sqrt((customer1[1] - customer2[1])**2 + (customer1[2] - customer2[2])**2)

######### TODO replace may with list comperhensions

def grade(input_data, quality_data, submission):
    score = 0
    scoreUB = 1.0
    feedback = ''

    lines = input_data.split('\n')

    parts = lines[0].split()
    customerCount = int(parts[0])
    vehicleCount = int(parts[1])
    vehicleCapacity = int(parts[2])
    depotIndex = 0

    customers = []
    for i in range(1,customerCount+1):
        line = lines[i]
        parts = line.split()
        customers.append((int(parts[0]), float(parts[1]), float(parts[2])))

    subLines = submission.splitlines();
    if(len(subLines) != vehicleCount+2) :
        return {'score':0.0, 'feedback':'output should have '+str(vehicleCount+1)+' lines, this one has '+str(len(subLines)-1)}

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

    tours = []
    for v in range(0, vehicleCount):
        vtour = subLines[1+v].split()

        if len(vtour) < 2 :
            return {'score':0.0, 'feedback':'the vehicle output line '+str(v)+' should have at least 2 values, this one has '+str(len(vtour))}

        badVals = set()
        for val in vtour:
            if not val.isdigit():
                badVals.add(val)
        if len(badVals) > 0:
            return {'score':0.0, 'feedback':'the vehicle output line '+str(v)+' should only contain integers, this output has the following bad values: '+(', '.join([str(x) for x in badVals]))}

        vtour = [int(x) for x in vtour]
        badVals = set()
        for val in vtour:
            if val < 0 or val > customerCount-1:
                badVals.add(val)
        if len(badVals) > 0:
            return {'score':0.0, 'feedback':'the vehicle output line '+str(v)+' should only contain values between 0 and '+str(customerCount-1)+', this output has the following bad values: '+(', '.join([str(x) for x in badVals]))}

        if vtour[0] != depotIndex:
            return {'score':0.0, 'feedback':'the vehicle output line '+str(v)+' does not start at the depot. The line should begin with the value '+str(depotIndex)+' but it starts with the value '+str(vtour[0])}

        if vtour[-1] != depotIndex:
            return {'score':0.0, 'feedback':'the vehicle output line '+str(v)+' does not end at the depot. The line should end with the value '+str(depotIndex)+' but it ends with the value '+str(vtour[-1])}

        tours.append(vtour)

    try:
        runtime = float(subLines[-1])
    except (ValueError, TypeError):
        return {'score':0.0, 'feedback': 'The evaluation script has failed with error code (2).  Sorry for the inconvenience.  Please post this message in the \'Platform Feedback\' forum.'+feedback}


    unused = set(range(0, customerCount))
    unused.discard(depotIndex)
    for vtour in tours:
        for c in vtour:
            unused.discard(c)

    if len(unused) > 0:
        return {'score':0.0, 'feedback':'the solution does not contain all of the customers in 0..'+str(customerCount-1)+', this solution is missing: '+(', '.join([str(x) for x in unused]))}

    totalCustomers = sum([len(vtour)-2 for vtour in tours])
    if totalCustomers != customerCount-1:
        return {'score':0.0, 'feedback':'the solution contains '+str(totalCustomers)+' customers, but only '+str(customerCount-1)+' are required.' }


    load = [0]*vehicleCount
    value = 0
    for v in range(0, vehicleCount):
        vtour = tours[v]
        for i in range(0, len(vtour)-1):
            load[v] += customers[vtour[i]][0]
            value += length(customers[vtour[i]],customers[vtour[i+1]])

    overloaded = []
    for v in range(0,vehicleCount):
        if load[v] > vehicleCapacity:
            overloaded.append('vehicle '+str(v)+' is over the capacity limit by '+str(load[v]-vehicleCapacity))
    if len(overloaded) > 0:
        return {'score':0.0, 'feedback':'the solution has vehicle capacity violations: '+', '.join(overloaded)}

    #print obj, value
    if abs(value - obj) > 1 :
        feedback = feedback + '\nWarning: submitted objective value is inconsistent with actual value. given: '+str(obj)+' actual value: '+str(value)

    # if opt :
    #     results = db.checkForLess(metadata.assignment_id, problem_id, value)
    #     if results != None and len(results) > 0 : # todo we should make this a little mode robust to floating point arithmetic
    #         bestVal = min([x[4] for x in results]) #4 is the quality column in the DB
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


