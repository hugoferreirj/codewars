#This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
#seven(times(five())) # must return 35
#four(plus(nine())) # must return 13
#eight(minus(three())) # must return 5
#six(divided_by(two())) # must return 3
#Requirements:
#
#There must be a function for each number from 0 ("zero") to 9 ("nine")
#There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
#Each calculation consist of exactly one operation and two numbers
#The most outer function represents the left operand, the most inner function represents the right operand
#Division should be integer division. For example, this should return 2, not 2.666666...:
#eight(divided_by(three()))

#My Solution
def doTheOperation(fullOperation):
    if fullOperation[1] == "+":
        return fullOperation[2] + fullOperation[0]
    elif fullOperation[1] == "-":
        return fullOperation[2] - fullOperation[0]
    elif fullOperation[1] == "*":
        return fullOperation[2] * fullOperation[0]
    elif fullOperation[1] == "//":
        return fullOperation[2] // fullOperation[0]
    else:
        print("Operator not found")
    

def zero(rightOperand=[]):
    if not rightOperand:
        return 0
    else:
        rightOperand.append(0)
        return doTheOperation(rightOperand)
def one(rightOperand=[]):
    if not rightOperand:
        return 1
    else:
        rightOperand.append(1)
        return doTheOperation(rightOperand)
def two(rightOperand=[]):
    if not rightOperand:
        return 2
    else:
        rightOperand.append(2)
        return doTheOperation(rightOperand)
def three(rightOperand=[]):
    if not rightOperand:
        return 3
    else:
        rightOperand.append(3)
        return doTheOperation(rightOperand)
def four(rightOperand=[]):
    if not rightOperand:
        return 4
    else:
        rightOperand.append(4)
        return doTheOperation(rightOperand)
def five(rightOperand=[]):
    if not rightOperand:
        return 5
    else:
        rightOperand.append(5)
        return doTheOperation(rightOperand)
def six(rightOperand=[]):
    if not rightOperand:
        return 6
    else:
        rightOperand.append(6)
        return doTheOperation(rightOperand)
def seven(rightOperand=[]):
    if not rightOperand:
        return 7
    else:
        rightOperand.append(7)
        return doTheOperation(rightOperand)
def eight(rightOperand=[]):
    if not rightOperand:
        return 8
    else:
        rightOperand.append(8)
        return doTheOperation(rightOperand)
def nine(rightOperand=[]):
    if not rightOperand:
        return 9
    else:
        rightOperand.append(9)
        return doTheOperation(rightOperand)

def plus(rightOperand, leftOperand="empty"):
    return [rightOperand, "+"]
def minus(rightOperand, leftOperand="empty"): 
    return [rightOperand, "-"]
def times(rightOperand, leftOperand="empty"):
    return [rightOperand, "*"]
def divided_by(rightOperand):
    return [rightOperand, "//"]
