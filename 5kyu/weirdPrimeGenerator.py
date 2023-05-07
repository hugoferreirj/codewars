#Consider the sequence a(1) = 7, a(n) = a(n-1) + gcd(n, a(n-1)) for n >= 2:
#
#7, 8, 9, 10, 15, 18, 19, 20, 21, 22, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 69, 72, 73....
#
#Let us take the differences between successive elements of the sequence and get a second sequence g: 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1....
#
#For the sake of uniformity of the lengths of sequences we add a 1 at the head of g:
#
#g: 1, 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1...
#
#Removing the 1s gives a third sequence: p: 5, 3, 11, 3, 23, 3... where you can see prime numbers.
#
#Task:
#Write functions:
#
#1: an(n) with parameter n: returns the first n terms of the series of a(n) (not tested)
#
#2: gn(n) with parameter n: returns the first n terms of the series of g(n) (not tested)
#
#3: countOnes(n) with parameter n: returns the number of 1 in the series gn(n) 
#    (don't forget to add a `1` at the head) # (tested)
#    
#4:  p(n) with parameter n: returns an array filled with the n first distinct primes in the same order they are found in the sequence gn (not tested)
#
#5: maxPn(n) with parameter n: returns the biggest prime number of the above p(n) # (tested)
#
#6: anOver(n) with parameter n: returns an array (n terms) of the a(i)/i for every i such g(i) != 1 (not tested but interesting result)
#
#7: anOverAverage(n) with parameter n: returns as an *integer* the average of anOver(n) # (tested)


#My Solution
import math

def aF(n,  aPredecessor):
    if n == 1:
        return 7
    elif n > 1:
        return aPredecessor + math.gcd(n, aPredecessor)

def an(n):
    if n:
        a = []
        predecessor = 0
        for i in range(1, n + 1):
            sucessor = aF(i, predecessor)
            a.append(sucessor)
            predecessor = sucessor
        return a
    return []

def gn(n):
    a = an(n)
    return [1] + [a[i+1] - a[i] for i in range(n-1)]

def count_ones(n):
    return gn(n).count(1)

def p(n):
    array = []
    i = 1
    predecessor = 0
    while len(array) < n:
        sucessor = aF(i, predecessor)
        if predecessor > 0:
            prime = sucessor - predecessor
            if prime != 1 and prime not in array:
                array.append(prime)
        predecessor = sucessor
        i += 1
    return array
    
def max_pn(n):
    return max(p(n))

def an_over(n):
    array = []
    i = 1
    predecessor = 0
    while len(array) < n:
        sucessor = aF(i, predecessor)
        if predecessor > 0:
            if sucessor - predecessor != 1:
                array.append(sucessor/i)
        predecessor = sucessor
        i += 1
    return array

def an_over_average(n):
    array = an_over(n)
    if array != []:
        return sum(array)//n
    return 0