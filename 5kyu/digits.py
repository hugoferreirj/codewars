from itertools import permutations
digits = [j for j in range(10)]
perms = list(permutations(digits, 4))
testedV = [] #tested Valid seqs
oldMatches = []
toTestU = [] #to test Unvalid seqs, with -1 inside them
testedU = [] #tested Unvalid seqs
answer = [-1, -1, -1, -1]
sMatch = False #searching Match

def possibleMatches(seqWithMatches, numberOfMatches):
    global sMatch, answer, toTestU
    print("seqMatches = " + str(seqWithMatches))
    sMatch = True
    for i in range(4):
        if answer[i] == -1:
            copySeq = list(seqWithMatches)
            copySeq[i] = -1
            toTestU.append(tuple(copySeq))
    print(toTestU)

def guess(matches):
    global perms, lastSeq, sMatch, toTestU, testedV, oldMatches, testedU, answer
    if sMatch and matches == oldMatches[-1]:
        print(toTestU)
        ind = testedU[-1].index(-1)
        print(testedV[-1][ind])
        print("not the match")
        for perm in perms[:]:
            if perm[ind] == testedV[-1][ind]:
                perms.remove(perm)
            else: 
                print(perm)
        if len(toTestU) > 0:
            testedU.append(toTestU[-1])
            return toTestU.pop()
        else:
            sMatch = False
    elif sMatch and matches < oldMatches[-1]:
        print(toTestU)
        ind = testedU[-1].index(-1)
        answer[ind] = testedV[-1][ind]
        print(answer)
        for perm in perms[:]:
                if perm[ind] != testedV[-1][ind]:
                    perms.remove(perm)
                else: 
                    print(perm)
        if len(toTestU) > 0: #(len(answer) - answer.count(-1)) < oldMatches[-1]:
            testedU.append(toTestU[-1])
            return toTestU.pop()
        else:
            sMatch = False
    elif matches > -1:
        oldMatches.append(matches)
        perms = perms[1:]
        print("matches = " + str(matches) +  " oldMatches = " + str(oldMatches))
        print("testedV = " + str(testedV))
        if matches == 0 or (len(answer) - answer.count(-1)) == oldMatches[-1]:
            print("new matches == 0")
            i = 1
            for perm in perms[:]:
                if perm[0] == testedV[-1][0] != answer[0] or perm[1] == testedV[-1][1] != answer[1] or perm[2] == testedV[-1][2] != answer[2] or perm[3] == testedV[-1][3]  != answer[3]:
                    perms.remove(perm)
                else:
                    print(str(i) + " " + str(perm))
                    i+=1
        elif (len(oldMatches) == 1 and matches > 0) or matches > oldMatches[-2]:
            i = 1
            print("new matches > 0")
            #for perm in perms[:]:
            #    if perm[0] != testedV[-1][0] and perm[1] != testedV[-1][1] and perm[2] != testedV[-1][2] and perm[3] != testedV[-1][3]:
            #        perms.remove(perm)
            #    else:
            #        print(str(i) + " " + str(perm))
            #        i+=1
            possibleMatches(testedV[-1], matches)
            nextSeq = toTestU.pop()
            testedU.append(nextSeq)
            return nextSeq
    testedV.append(perms[0])
    return perms[0] 