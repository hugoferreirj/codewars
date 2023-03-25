#Write Number in Expanded Form
#You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'
#note: All numbers will be whole numbers greater than 0.


#My Solution
def expandTheNumber(number, powerOfTen):
    return int(number) * powerOfTen

def expanded_form(num):
    numAsString = str(num)
    expandedForm = []
    lenNum = len(numAsString)
    for i in range(lenNum):
        if(numAsString[i] != "0"):
            powerOfTen = 10**(lenNum-(i+1))
            expandedForm.append(str(expandTheNumber(numAsString[i], powerOfTen)))
    return " + ".join(expandedForm)
   
#Explaining:
#First we turn the number into a string. This way we can isolate the decimal places
#After we get the lenght of the number to identify how many decimal places it has
#Then we enter the loop where we calculate the powerOfThen that the isolated 
#Decimal place needs to be multiplied to expand the number
#We send it to a function where it is expanded
#Finally we turn it into a string and added to a list with all the other expanded 
#Numbers
#When everything is done, we turn the list into a string where all the expanded numbers
#Are separated by " + "