#Given an array of integers, find the one that appears an odd number of times.
#
#There will always be only one integer that appears an odd number of times.
#
#Examples
#[7] should return 7, because it occurs 1 time (which is odd).
#[0] should return 0, because it occurs 1 time (which is odd).
#[1,1,2] should return 2, because it occurs 1 time (which is odd).
#[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
#[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

#My Solution
def find_it(seq):
    sortedSeq = sorted(seq)
    count = 0
    for i in sorted(set(seq)):
        for j in sortedSeq:
            if i == j:
                count+=1
                sortedSeq = sortedSeq[1:] #remove thee item already counted
            else:
                break
        if (count % 2) == 1 or count == 1:
            return i
        else:
            count = 0
    return None
