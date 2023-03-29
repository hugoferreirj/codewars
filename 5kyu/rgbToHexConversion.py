#The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
#
#Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
#The following are examples of expected output values:
#
#rgb(255, 255, 255) # returns FFFFFF
#rgb(255, 255, 300) # returns FFFFFF
#rgb(0,0,0) # returns 000000
#rgb(148, 0, 211) # returns 9400D3

#My Solution

def decimalToHexa(value):
    hexa = ""
    for i in range(2):
        rest = value % 16
        if rest == 10:
            hexa = "A" + hexa
        elif rest == 11:
            hexa = "B" + hexa
        elif rest == 12:
            hexa = "C" + hexa
        elif rest == 13:
            hexa = "D" + hexa
        elif rest == 14:
            hexa = "E" + hexa
        elif rest == 15:
            hexa = "F" + hexa
        else:
            hexa = str(rest) + hexa
        value = value // 16
    return hexa
            
        

def rgb(r, g, b):
    rgbList = [r, g, b]
    hexa = ""
    for x in rgbList:
        if x < 0:
            x = 0
        elif x > 255:
            x = 255
        hexa += decimalToHexa(x)
    return hexa