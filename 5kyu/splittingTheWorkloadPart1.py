import itertools as it

def split_list(xs):
    a, b, subt = [], [], [] 
    #create all the possible two lists and then calculate the subtraction
    for pattern in it.product([True, False], repeat=len(xs)):
        a.append([x[1] for x in zip(pattern, xs) if x[0]])
        b.append([x[1] for x in zip(pattern, xs) if not x[0]])
        subt.append(abs(sum(a[-1]) - sum(b[-1])))
        if subt[-1] == 0:
            return a[-1],b[-1]
    minimised = min(subt)
    index = subt.index(minimised)
    return a[index],b[index]
