#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
#
#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice

#My Solution

def duplicate_count(text):
    if text != "":
        characs = sorted(list(text.lower())) #splited and sorted lower case character
        count = 0 #count the distinct case-insensitive alphabetic characters and numeric digits that occur more than once
        lastChar = characs[0] #last character visited
        lastCharCounted = ""
        for i in range(1,len(characs)):
            if characs[i] == lastChar and lastCharCounted != characs[i]:
                count+=1
                lastCharCounted = characs[i]
            lastChar = characs[i]
        return count