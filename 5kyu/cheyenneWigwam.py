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
                drawing[i][length - numberOfRows + i] = "\\"
                if i == 2:
                    drawing[i][middle] = "°"
                elif i == numberOfRows - 2:
                    drawing[i][middle-1] = "/"
                    drawing[i][middle] = "‾"
                    drawing[i][middle+1] = "\\"
                elif i == numberOfRows - 1:
                    drawing[i][middle-2] = "/"
                    drawing[i][middle+2] = "\\"
        d = ["".join(row) for row in drawing]
        return "\n".join(d)