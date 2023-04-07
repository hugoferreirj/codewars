#not completed, try this later

import math

def calculateRepetition(word):
    repetition = dict()
    for char in word:
        if repetetion.get(char) == None:
            repetition[char] = 1
        else:
            repetition[char] += 1
    return repetition

def listPosition(word):
    word = list(word)
    sortedWord = sorted(word)
    repetition = calculateRepetition(word)
    if word == sortedWord:
        return 1
    else:
        positionLetter = sortedWord.index(word[0]) #get the position of the first word in the sortedWord
        result = positionLetter*math.fatorial(word.lenght() - 1)/math.fatorial
   