#Task
#You are given an odd integer n and a two-dimensional array s, which contains n equal-sized arrays of 0s and 1s.
#
#Return an array of the same length as the elements of n, such that its ith element is the one that appears most frequently at the ith position of s' elements.
#
#Code Limit
#Less than 55 characters.
#
#Example
#For n = 3, s = [[1,1,0], [1,0,0], [0,1,1]],
#
#the output should be [1,1,0]
#
#1st  2nd  3rd
# 1    1    0
# 1    0    0
# 0    1    1
# 
#
#At the 1st position 
#there're two 1s and one 0, 
#so in the 1st element of the resulting array is 1.
#
#At the 2nd position
#there're two 1s and one 0,
#so in the 2nd element of the resulting array is 1.
#
#At the 3rd position 
#there're two 0s and one 1, 
#so in the 3rd element of the resulting array is 0.

#couldn't solve this one, but here's the solution provided:

#zip(*s), s being a nested list, returns a list of tuples. each tuple contain the elements of each columns of the array:
#example: s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#zip(*s) = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

zero_or_one=lambda n,s:[sum(x)>n/2for x in zip(*s)]