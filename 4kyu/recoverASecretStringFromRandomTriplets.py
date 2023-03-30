#There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.
#
#A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
#
#As a simplification, you may assume that no letter occurs more than once in the secret string.
#
#You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

def recoverSecret(triplets):
    lettersSecret = []
    secret = ""
    desiredLetter = True
    for triplet in triplets: #concatenate all the triplets
        lettersSecret += triplet
    lettersSecret = list(set(lettersSecret)) #remove repetition
    while lettersSecret: #everytime a letter's place is found, it is removed from lettersSecets
        for letter in lettersSecret: 
            for triplet in triplets: 
                if len(triplet)>1:
                    if letter in triplet[1:]: #if the letter follows any other, it's not what we're looking for
                        desiredLetter = False
                        break
            if desiredLetter: #if the letter doesn't follows any other
                secret += letter
                for triplet in triplets:
                    if len(triplet)>0:
                        if letter in triplet:
                            triplet.remove(letter)
                lettersSecret.remove(letter)
                break
            desiredLetter = True
    return secret