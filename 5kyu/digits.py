from itertools import permutations
digits = [j for j in range(10)]
perms = list(permutations(digits, 4))
tested = []
matched = []

def guess(matches):
    global perms
    global lastSeq
    print(tested)
    #print(perms[:4])
    if matches > -1:
        matched.append(matches)
        perms = perms[1:]
        if matches == 0:
            print("matches == 0")
            i = 1
            for perm in perms[:]:
                if perm[0] == tested[-1][0] or perm[1] == tested[-1][1] or perm[2] == tested[-1][2] or perm[3] == tested[-1][3]:
                    perms.remove(perm)
                else:
                    print(str(i) + " " + str(perm))
                    i+=1
        #tem um erro aqui
        elif len(matched) > 1 and matches == matched[-2]:
            print("matches == matched[-2]")
            i = 1
            for perm in perms[:]:
                if perm[0] != tested[-2][0] == tested[-1][0] or perm[1] != tested[-2][1] == tested[-1][1] or perm[2] != tested[-2][2] == tested[-1][2] or perm[3] != tested[-2][3] == tested[-1][3]:
                    perms.remove(perm)
                else:
                    print(str(i) + " " + str(perm))
                    i+=1
        #tem um erro aqui
        elif len(matched) > 1 and matches <= matched[-2]:
            print("matches < matched[-2]")
            i = 1
            for perm in perms[:]:
                if perm[0] == tested[-1][0] != tested[-2][0] or perm[1] == tested[-1][1] != tested[-2][1] or perm[2] == tested[-1][2] != tested[-2][2] or perm[3] == tested[-1][3] != tested[-2][3]:
                    perms.remove(perm)
                else:
                    print(str(i) + " " + str(perm))
                    i+=1
        elif matches > 0:
            i = 1
            print("start printing Match > 1")
            for perm in perms[:]:
                if perm[0] != tested[-1][0] and perm[1] != tested[-1][1] and perm[2] != tested[-1][2] and perm[3] != tested[-1][3]:
                    perms.remove(perm)
                else:
                    print(str(i) + " " + str(perm))
                    i+=1
    tested.append(perms[0])
    return perms[0] 