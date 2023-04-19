from itertools import permutations
digits = [j for j in range(10)]
perms = list(permutations(digits, 4))
lastMatch = 0
listaTeste = [1, 2, 3, 4, 5]


def guess(matches):
    print(listaTeste)
    lastTry = perms[0]
    if matches == 0:
        # print("start printing")
        i = 1
        for perm in perms:
            if perm[0] == lastTry[0] or perm[1] == lastTry[1] or perm[2] == lastTry[2] or perm[3] == lastTry[3]:
                perms.remove(perm)
            else:
                # print(str(i) + " " + str(perm))
                i += 1
    elif matches > 0:
        i = 1
        # print("start printing Match > 1")
        for perm in perms:
            if perm[0] != lastTry[0] and perm[1] != lastTry[1] and perm[2] != lastTry[2] and perm[3] != lastTry[3]:
                perms.remove(perm)
            else:
                # print(str(i) + " " + str(perm))
                i += 1
    if listaTeste > 1:
        listaTeste = listaTeste[1:]
    return perms[0]
