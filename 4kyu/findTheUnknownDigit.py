def calculate(firstElement, secondElement, operator):
    if operator == "*": return firstElement * secondElement
    elif operator == "+": return firstElement + secondElement
    elif operator == "-": return firstElement - secondElement
    else: return False

def possibilities(element, digitsUncovered):
    if "?" in element:
        elements = []
        invalidValue = 1000001
        for digit in digitsUncovered:
            #exclude possibilities like 00, -0, 032, -09, (numbers starting with 0)
            if digit == "0" and len(element) > 1 and (element[0] == "?" or (element[0] == "-" and element[1] == "?")):
                elements.append(invalidValue) #if it begin with a 0 and the number itself isn't 0, for example 00
            else:
                possibility = element.replace("?", digit)
                elements.append(int(possibility))
        return elements
    else:
        return [int(element) for digit in digitsUncovered]

def couldBeTheDigit(firstE, secondE, result, operator):
    if -1000000 <= firstE <= 1000000 and -1000000 <= secondE <= 1000000 and -1000000 <= result <= 1000000:
        if calculate(firstE, secondE, operator) == result:
            return True
    return False

def solve_runes(runes):
    digitsUncovered = [str(i) for i in range(10) if str(i) not in set(runes)]
    if "*" in runes:
        operatorIndex = runes.index("*")
    elif "+" in runes:
        operatorIndex = runes.index("+")
    elif "-" in runes[1:]: #start looking from 1 because we don't want to take the sign of first element
        operatorIndex = runes.index("-", 1)
    else:
        return -1
    if "=" in runes: 
        equalIndex = runes.index("=")
        pFirstElements = possibilities(runes[:operatorIndex], digitsUncovered)
        pSecondElements = possibilities(runes[operatorIndex + 1: equalIndex], digitsUncovered)
        pResults = possibilities(runes[equalIndex + 1:], digitsUncovered)
        for i in range(len(digitsUncovered)):
            if couldBeTheDigit(pFirstElements[i], pSecondElements[i], pResults[i], runes[operatorIndex]):
                return int(digitsUncovered[i])
        return -1       
    else: #no equal sign found
        return -1
