#Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:
#
#['XOOXO',
# 'XOOXO',
# 'OOOXO',
# 'XXOXO',
# 'OXOOO'] 

#should return: "Total land perimeter: 24".
#
#Following input:
#
#['XOOO',
# 'XOXO',
# 'XOXO',
# 'OOXX',
# 'OOOO']
#should return: "Total land perimeter: 18"

#My Solution
def land_perimeter(arr):
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X": #checks if each point is an X, and for each side that it's not followed by an X, sum 1 to the perimeter
                if j+1>=len(arr[i]) or arr[i][j+1] == "O":
                    perimeter += 1
                if j-1<0 or arr[i][j-1] == "O":
                    perimeter += 1
                if i-1<0 or arr[i-1][j] == "O":
                    perimeter += 1
                if i+1>=len(arr) or arr[i+1][j] == "O":
                    perimeter += 1
    return "Total land perimeter: " + str(perimeter)
                
            
    
