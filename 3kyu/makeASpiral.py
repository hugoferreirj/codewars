#we can understand where we are in the array looking at row and col values

def goRight(row, start, end): #define element = 0 from start, inclusive, till < end, left to right
    for i in range(start, end):
        row[i] = 0

def goDown(array, indexCol, start, end): #define element = 0 from start, inclusive, till < end, from up to down
    for i in range(start, end):           
        array[i][indexCol] = 0

def spiralize(size):
    spiral = [[1 for i in range(size)] for j in range(size)] #create all rows filled with 1
    steps = size - 1 #how many we need to walk right||down||left||up
    row = 1 #row 0 is always all filled with 1
    col = 0
    while steps > 0:
        goRight(spiral[row], col, col + steps)
        col += steps - 1 #goRight changed values till index < col+steps, so we're at col + steps - 1
        steps -= 2
        if steps <= 0:
            break
        goDown(spiral, col, row + 1, row + steps + 1)
        row += steps
        goRight(spiral[row], col - steps, col) #we are "walking" left, but we're changing the array from left to right
        col -= steps
        steps -= 2
        if steps <= 0:
            break
        goDown(spiral, col, row - steps, row) #we are "walking" up, but we're changing the array from up to down
        row -= steps
        col += 1
    return spiral