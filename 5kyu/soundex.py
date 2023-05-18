#A History Lesson
#Soundex is an interesting phonetic algorithm developed nearly 100 years ago for indexing names as they are pronounced in English. The goal is for homophones to be encoded to the same representation so that they can be matched despite minor differences in spelling.
#
#Reference: https://en.wikipedia.org/wiki/Soundex
#
#Preface
#I first read about Soundex over 30 years ago. At the time it seemed to me almost like A.I. that you could just type in somebody's name the way it sounded and there was still a pretty good chance it could match the correct person record. That was about the same year as the first "Terminator" movie so it was easy for me to put 2 and 2 together and conclude that Arnie must have had some kind of futuristic Soundex chip in his titanium skull helping him to locate Serah Coner... or was it Sarh Connor... or maybe Sayra Cunnarr...
#
#:-)
#
#Task
#In this Kata you will encode strings using a Soundex variation called "American Soundex" using the following (case insensitive) steps:
#
#Save the first letter. Remove all occurrences of h and w except first letter.
#Replace all consonants (include the first letter) with digits as follows:
#b, f, p, v = 1
#c, g, j, k, q, s, x, z = 2
#d, t = 3
#l = 4
#m, n = 5
#r = 6
#Replace all adjacent same digits with one digit.
#Remove all occurrences of a, e, i, o, u, y except first letter.
#If first symbol is a digit replace it with letter saved on step 1.
#Append 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it
#Input
#A space separated string of one or more names. E.g.
#
#Sarah Connor
#
#Output
#Space separated string of equivalent Soundex codes (the first character of each code must be uppercase). E.g.
#
#S600 C560

#My Solution
import re

hw = ["h", "H", "W", "w"]
bfpv = ["b", "f", "p", "v", "B", "F", "P", "V"]
cgjkqsxz = ["c", "g", "j", "k", "q", "s", "x", "z", "C", "G", "J", "K", "Q", "S", "X", "Z"]
dt = ["d", "t", "D", "T"]
l = ["l", "L"]
mn = ["m", "n", "M", "N"]
r = ["r", "R"]
aeiouy = ["a", "e", "i", "o", "u", "y", "A", "E", "Y", "O", "U", "Y"]

def replaceAdjacentSameDigits(word):
    lastChar = "9999999999"
    finalWord = ""
    for char in word:
        if char != lastChar:
            finalWord += char
        lastChar = char
    return finalWord

def removeAllOcurrences(word, chars):
    for char in chars:
        word = word.replace(char, "")
    return word

def replaceAllOcurrences(word, chars, sub):
    for char in chars:
        word = word.replace(char, sub)
    return word

def addZeros(word):
    while len(word) < 4:
        word = word + "0"
    return word

def replaceLetters(word):
    word = replaceAllOcurrences(word, bfpv, "1")
    word = replaceAllOcurrences(word, cgjkqsxz, "2")
    word = replaceAllOcurrences(word, dt, "3")
    word = replaceAllOcurrences(word, l, "4")
    word = replaceAllOcurrences(word, mn, "5")
    word = replaceAllOcurrences(word, r, "6")
    return word

def soundex(name):
    words = name.split()
    firstLetters = [l[0] for l in words] #save first Letters
    for i, word in enumerate(words[:]):
        words[i] = removeAllOcurrences(words[i], hw)
        words[i] = replaceLetters(words[i])
        words[i] = replaceAdjacentSameDigits(words[i])
        words[i] = removeAllOcurrences(words[i], aeiouy)
        if firstLetters[i] in hw or firstLetters[i] in aeiouy:
            words[i] = firstLetters[i] + words[i]
        else:
            words[i] = firstLetters[i] + words[i][1:]
        words[i] = addZeros(words[i])
        words[i] = words[i][:4].upper()
    return " ".join(words)


