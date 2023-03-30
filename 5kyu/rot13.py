#ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
#Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
#Please note that using encode is considered cheating.

def rot13(message):
    alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = False
    finalSentence = ""
    for charac in message:
        if charac.isupper():
            charac = charac.lower()
            upper = True
        try:
            index = alphabet.index(charac)
            index13after = (index + 13) % 26
            if upper:
                finalSentence = finalSentence + alphabet[index13after].upper()
                upper = False
            else:
                finalSentence = finalSentence + alphabet[index13after]
        except ValueError as ve:
            finalSentence = finalSentence + charac
    return finalSentence