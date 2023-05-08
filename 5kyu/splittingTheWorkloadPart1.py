#Imagine you have a number of jobs to execute. Your workers are not permanently connected to your network, so you have to distribute all your jobs in the beginning. Luckily, you know exactly how long each job is going to take.
#
#Let
#
#x = [2,3,4,6,8,2]
#be the amount of time each of your jobs is going to take.
#
#Your task is to write a function splitlist(x), that will return two lists a and b, such that abs(sum(a)-sum(b)) is minimised.
#
#One possible solution to this example would be
#
#a=[2, 4, 6]
#b=[3, 8, 2]
#with abs(sum(a)-sum(b)) == 1.
#
#The order of the elements is not tested, just make sure that you minimise abs(sum(a)-sum(b)) and that sorted(a+b)==sorted(x).
#
#You may assume that len(x)<=15 and 0<=x[i]<=100.
#
#When done, please continue with part II!

#My Solution

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
