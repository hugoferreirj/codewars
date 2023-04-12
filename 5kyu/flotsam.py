def notPartOfShipNorWater(charac):
    return charac in [" ", "S", "T", "F", "x"]
    
def dieIfPassenger(charac, p):
    if charac == "F": p = p.remove("Frank")
    elif charac == "S": p = p.remove("Sam")
    elif charac == "T": p = p.remove("Tom")

def aroundWater(image, i, j, nOfRows, nOfCols):
    if i > 0 and image[i-1][j] == "~": return True
    elif j > 0 and image[i][j-1] == "~": return True
    elif i + 1 < nOfRows and image[i+1][j] == "~": return True
    elif j + 1 < nOfCols and image[i][j+1] == "~": return True
    else: return False


def fillOrthogonalD(i, j , nOfRows, nOfCols, levelWater, image, p):
    u, d = i, i #up and down
    l, r = j, j #left and right
    while u - 1 >= 0 and u-1 >= levelWater and notPartOfShipNorWater(image[u-1][j]):
        dieIfPassenger(image[u-1][j], p)
        image[u-1][j] = "~"
        u -= 1
        fillOrthogonalD(u, j, nOfRows, nOfCols, levelWater, image, p)
    while d + 1 < nOfRows and d+1 >= levelWater and notPartOfShipNorWater(image[d+1][j]):
        dieIfPassenger(image[d+1][j], p)
        image[d+1][j] = "~"
        d += 1
        fillOrthogonalD(d, j, nOfRows, nOfCols, levelWater, image, p)
    while l - 1 >= 0 and notPartOfShipNorWater(image[i][l-1]):
        dieIfPassenger(image[i][l-1], p)
        image[i][l-1] = "~"
        l -= 1
        fillOrthogonalD(i, l, nOfRows, nOfCols, levelWater, image, p)
    while r + 1 < nOfCols and notPartOfShipNorWater(image[i][r+1]):
        dieIfPassenger(image[i][r+1], p)
        image[i][r+1] = "~"
        r += 1
        fillOrthogonalD(i, r, nOfRows, nOfCols, levelWater, image, p)
    
def flotsam(image):
    nOfRows = len(image)
    nOfCols = len(image[0])
    levelWater = -1
    passengers = ["Frank", "Sam", "Tom"]
    for i in range(nOfRows):
        for j in range(nOfCols):
            if image[i][j] == "~" and levelWater == -1: #find the level of water
                levelWater = i
            if image[i][j] == "x" and -1 < levelWater <= i and aroundWater(image, i, j, nOfRows, nOfCols):
                fillOrthogonalD(i, j , nOfRows, nOfCols,levelWater, image, passengers)
    return " ".join(passengers)
