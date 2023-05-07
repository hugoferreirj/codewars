#There are a n balls numbered from 0 to n-1 (0,1,2,3,etc). Most of them have the same weight, but one is heavier. Your task is to find it.
#
#Your function will receive two arguments - a scales object, and a ball count. The scales object has only one method:
#
#    get_weight(left, right)
#where left and right are arrays (or lists, vectors ...) of numbers of balls to put on left and right pan respectively.
#
#If the method returns -1 - left pan is heavier
#
#If the method returns 1 - right pan is heavier
#
#If the method returns 0 - both pans weigh the same
#
#So what makes this the "ubermaster" version of this kata? First, it's not restricted to 8 balls as in the previous versions - your solution has to work for 8-500 balls.
#
#Second, you can't use the scale any more than mathematically necessary. Here's a chart:
#
#ball count | uses
#-----------------
#       0-9 |    2
#     10-27 |    3
#     28-81 |    4
#    82-243 |    5
#   244-500 |    6


#My Solution
def find_ball(scales, ball_count):
    fullL = [i for i in range(ball_count)]
    left, right = -1, 1
    while ball_count > 0:
        if ball_count == 2:
            s = ball_count//2
        else:
            s = ball_count//3 #separe
        leftL = [fullL[i] for i in range(0, s)]
        rightL = [fullL[i] for i in range(s, s + s)]
        restL = [fullL[i] for i in range(s + s, ball_count)]
        heavier = scales.get_weight(leftL, rightL)
        if heavier == left:
            if len(leftL) == 1:
                return leftL[0]
            else:
                ball_count = len(leftL)
                fullL = leftL
        elif heavier == right:
            if len(rightL) == 1:
                return rightL[0]
            else:
                ball_count = len(rightL)
                fullL = rightL
        else:
            if len(restL) == 1:
                return restL[0]
            else:
                ball_count = len(restL)
                fullL = restL
    