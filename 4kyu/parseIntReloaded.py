#In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
#
#Examples:
#
#"one" => 1
#"twenty" => 20
#"two hundred forty-six" => 246
#"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
#Additional Notes:
#
#The minimum number is "zero" (inclusively)
#The maximum number, which must be supported is 1 million (inclusively)
#The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
#All tested numbers are valid, you don't need to validate them

import re

def parse_int(string):
    number = 0 #save the final result
    aux = 0 #save numbers before we find "hundred", "thousand" or "million". when we find it we multiply it by what we found and sum it to "number"
    lastMultiplier = "thousand" #this var help to discover when hundred appears before thousand in the string
    dictionary = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
                    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
                    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
                    "hundred": 100, "thousand": 1000, "million": 1000000}
    for word in re.split("\W+", string):
        if word != "and":
            if word == "hundred" or word == "thousand" or word == "million":
                if aux == 0 or dictionary[lastMultiplier] < dictionary[word]: #if aux == 0, it means the last thing done was number multiplied by 100||1k||1kk. example: two HUNDRED thousand
                    if aux != 0: #for cases like forty hundred sixty-six thousand, when aux != 0, in this case aux == 66
                        number += aux
                    number *= dictionary[word]
                else:
                    number += aux*dictionary[word]
                lastMultiplier = word
                aux = 0
            else:
                aux += dictionary[word]
    return number + aux