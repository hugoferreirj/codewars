def drawTop(n):
    firstR = "".join([" " for i in range(n-1)] + ["\\*/"] + [" " for i in range(n-1)])
    secR = firstR.replace("\\*/", " ¥ ")
    thirdR = firstR.replace("\\*/", "/°\\")
    return [firstR, secR, thirdR]
                            
def draw_wigwam(n):
    if 3 <= n <= 100:
        numberOfRows = n + 2
        length = 2*n + 1
        middle = n
        drawing = [[" " for i in range(length)] for j in range(numberOfRows)]
        for i in range(numberOfRows):
            if i == 1:
                drawing[i][middle] = "¥"
            else:    
                drawing[i][numberOfRows - i - 1] = "/"
                for j in range(numberOfRows - i, length - numberOfRows + i):
                    if n>4 and i == n and (j == 3 or j == length - 4):
                        drawing[i][j] = "°"
                    elif n > 4 and i % 2 == 0 and i != n and drawing[i][j-1] == ":":
                        drawing[i][j] = "_"
                    elif n > 4 and i % 2 == 1 and i != n and drawing[i][j-1] == ":":
                        drawing[i][j] = "-"
                    else:
                        drawing[i][j] = ":"
                drawing[i][length - numberOfRows + i] = "\\"
                if i == 2:
                    drawing[i][middle] = "°"
                elif i == numberOfRows - 2:
                    drawing[i][middle-1] = "/"
                    drawing[i][middle] = "‾"
                    drawing[i][middle+1] = "\\"
                elif i == numberOfRows - 1:
                    drawing[i][middle-2] = "/"
                    drawing[i][middle-1] = " "
                    drawing[i][middle] = " "
                    drawing[i][middle+1] = " "
                    drawing[i][middle+2] = "\\"
        d = ["".join(row) for row in drawing]
        return "\n".join(d)

# procurando padrão
n = 3 - não tem - length = 7, numberOfRows = 5
n = 4 - não tem - length = 9, numberOfRows = 6
n = 5 -                                                                     [5][3] e [5][7] - length = 11, numberOfRows = 7
n = 6 -                                                            [5][6] e [6][3] e [6][9] - length = 13, numberOfRows = 8 
n = 7 -                                         [3][7] e           [5][7] e [7][3] e [7][11] - length = 15, numberOfRows = 9
n = 8 -                                         [4][7]  e[4][9] e  [5][8] e [8][3] e [8][13] - length = 17, numberOfRows = 10
n = 9 -                                [5][9] e [5][7] e [5][11] e [8][9] e [9][3] e [9][15] - length = 19, numberOfRows = 11
n = 10 -                               [5][10] e[6][7] e [6][13] e [8][10] e[10][3] e[10][17] - length = 21, numberOfRows = 12
n = 11 -                      [3][11] e[5][11]e [7][7] e [7][15] e [8][11] e[11][3] e[11][19] - length = 23, numberOfRows = 13
n = 12 -   [4][13]e [8][12]e  [4][11]  [5][12] e[8][7]  e[8][17] e [11][12]e[12][3] e[12][21] - length = 25, numberOfRows = 14
