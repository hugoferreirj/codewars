#Falta refatorar e tentar otimizar no tempo

from itertools import permutations
digits = [j for j in range(10)]
perms = list(permutations(digits, 4))
testedV = [] #tested Valid seqs
oldMatches = []
toTestU = [] #to test Unvalid seqs, with -1 inside them
testedU = [] #tested Unvalid seqs
answer = [-1, -1, -1, -1]
sMatch = False #searching Match

def restartGlobalVariables():
    global perms, lastSeq, sMatch, toTestU, testedV, oldMatches, testedU, answer
    digits = [j for j in range(10)]
    perms = list(permutations(digits, 4))
    testedV = [] 
    oldMatches = []
    toTestU = [] 
    testedU = [] 
    answer = [-1, -1, -1, -1]
    sMatch = False 
    
def possibleMatches(seqWithMatches, numberOfMatches):
    global sMatch, answer, toTestU
    sMatch = True
    for i in range(4):
        if answer[i] == -1:
            copySeq = list(seqWithMatches)
            copySeq[i] = -1
            toTestU.append(tuple(copySeq))

def removeImpossibleMatches():
    global toTestU, perms, testedU, testedV
    while toTestU:
        ind = toTestU[-1].index(-1)
        for perm in perms[:]:
            if perm[ind] == testedV[-1][ind]:
                perms.remove(perm)
        if len(toTestU) > 0:
            del toTestU[-1]

def foundPartsOfAnswer():
    global toTestU, perms, testedU, testedV
    while toTestU:
        ind = toTestU[-1].index(-1)
        answer[ind] = testedV[-1][ind]
        for perm in perms[:]:
                if perm[ind] != testedV[-1][ind]:
                    perms.remove(perm)
        if len(toTestU) > 0:
            del toTestU[-1]

def guess(matches):
    global perms, lastSeq, sMatch, toTestU, testedV, oldMatches, testedU, answer
    matchesFound = len(answer) - answer.count(-1)
    if matches == -1:
        restartGlobalVariables()
    if sMatch and (matches - matchesFound) == len(toTestU):
        foundPartsOfAnswer()
        sMatch = False
    elif sMatch and matches == oldMatches[-1]:
        ind = testedU[-1].index(-1)
        for perm in perms[:]:
            if perm[ind] == testedV[-1][ind]:
                perms.remove(perm)
        if len(toTestU) > 0:
            testedU.append(toTestU[-1])
            return toTestU.pop()
        else:
            sMatch = False
    elif sMatch and matches < oldMatches[-1]:
        ind = testedU[-1].index(-1)
        answer[ind] = testedV[-1][ind]
        for perm in perms[:]:
                if perm[ind] != testedV[-1][ind]:
                    perms.remove(perm)
        if (len(answer) - answer.count(-1)) < oldMatches[-1]:
            testedU.append(toTestU[-1])
            return toTestU.pop()
        else:
            removeImpossibleMatches()
            sMatch = False
    elif matches > -1:
        oldMatches.append(matches)
        perms = perms[1:]
        if matches == 0 or (len(answer) - answer.count(-1)) == oldMatches[-1]:
            for perm in perms[:]:
                if perm[0] == testedV[-1][0] != answer[0] or perm[1] == testedV[-1][1] != answer[1] or perm[2] == testedV[-1][2] != answer[2] or perm[3] == testedV[-1][3]  != answer[3]:
                    perms.remove(perm)
        elif (len(oldMatches) == 1 and matches > 0) or matches > oldMatches[-2]:
            possibleMatches(testedV[-1], matches)
            nextSeq = toTestU.pop()
            testedU.append(nextSeq)
            return nextSeq
    testedV.append(perms[0])
    return perms[0] 


#Shorter solution:

#import itertools
#
#def guess(n):
#    if n == -1:
#        # Start by guessing the first code in the list
#        guess.remaining_codes = list(itertools.permutations(range(10), 4))
#        guess.prev_guess = guess.remaining_codes[0]
#    else:
#        # Remove any code from the list that would not produce the same number of matches
#        guess.remaining_codes = [code for code in guess.remaining_codes
#                                      if sum(a == b for a, b in zip(code, guess.prev_guess)) == n]
#        # Choose the next code in the list and guess it
#        guess.prev_guess = guess.remaining_codes[0]
#    return list(guess.prev_guess)
#
#guess.remaining_codes = None
#guess.prev_guess = None