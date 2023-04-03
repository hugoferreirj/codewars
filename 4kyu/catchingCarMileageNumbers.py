#"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?
#
#Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).
#
#It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
#
#Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.
#
#"Interesting" Numbers
#Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
#
#Any digit followed by all zeros: 100, 90000
#Every digit is the same number: 1111
#The digits are sequential, incementing†: 1234
#The digits are sequential, decrementing‡: 4321
#The digits are a palindrome: 1221 or 73837
#The digits match one of the values in the awesome_phrases array
#† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
#‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
#
#So, you should expect these inputs and outputs:
#
## "boring" numbers
#is_interesting(3, [1337, 256])    # 0
#is_interesting(3236, [1337, 256]) # 0
#
## progress as we near an "interesting" number
#is_interesting(11207, []) # 0
#is_interesting(11208, []) # 0
#is_interesting(11209, []) # 1
#is_interesting(11210, []) # 1
#is_interesting(11211, []) # 2
#
## nearing a provided "awesome phrase"
#is_interesting(1335, [1337, 256]) # 1
#is_interesting(1336, [1337, 256]) # 1
#is_interesting(1337, [1337, 256]) # 2

#My Solution

def is_interesting(number, awesome_phrases):
    numberAsListOfDigits = list(str(number))
    if len(numberAsListOfDigits) > 1:
        firstDigit = int(numberAsListOfDigits[0])
        secondDigit = int(numberAsListOfDigits[1])
        lastDigit = int(numberAsListOfDigits[-1])
        if lastDigit == 0 and firstDigit<secondDigit: #this is used when checking if its a sequence of increasing number or dec number
            lastDigit = 10 #because the sequence is 01234567890, we'll just ignore the last digit if its = 0
            
    firstHalf = numberAsListOfDigits[:len(numberAsListOfDigits)//2]
    secondHalf = numberAsListOfDigits[len(numberAsListOfDigits)//2:]
    if len(numberAsListOfDigits)%2 != 0: #the digit in the middle doesnt count when we check if it is a palindrome 
        secondHalf = secondHalf[1:]
    secondHalf.reverse() #this will be used to discover if its a palindrome

    if number in awesome_phrases:
        return 2
    if len(numberAsListOfDigits)>=3:
        if len(set(numberAsListOfDigits)) == 1: #if every digit is the same
            return 2
        elif set(numberAsListOfDigits[1:]) == {'0'}: #any digit followed by all zeros
            return 2
        elif numberAsListOfDigits == [str(i) if i != 10 else "0" for i in range(firstDigit, lastDigit + 1)]: #The digits are sequential, incementing
            return 2
        elif numberAsListOfDigits == [str(i) if i != 10 else "0" for i in range(firstDigit, lastDigit - 1, -1)]: #The digits are sequential, decrementing
            return 2
        elif firstHalf == secondHalf: #palindrome, even number of digits
            return 2
    if awesome_phrases == [] or awesome_phrases[-1] != "nextTwoMileNumbers":
        awesome_phrases.append("nextTwoMileNumbers")  
        if is_interesting(number + 1, awesome_phrases) == 2 or is_interesting(number + 2, awesome_phrases) == 2: #an interesting number occurs within the next two miles
            return 1
        return 0
    else:
        return 0
        
        