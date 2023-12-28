import sys

def charCounter(inputString):
    numberOfEachChar = {}
    for char in inputString:
        if char not in numberOfEachChar:
            numberOfEachChar.update({char: 1})
        else:
            numberOfEachChar.update({char: numberOfEachChar.get(char) + 1})
    return numberOfEachChar

def wordCounter(inputString):
    inputString = inputString.lower()
    wordArray = inputString.split()
    wordDictionary = {}
    for word in wordArray:
        if word not in wordDictionary:
            wordDictionary.update({word:1})
        else:
            wordDictionary.update({word:wordDictionary.get(word)+1})
    return wordDictionary

print(charCounter("abca"))
print(wordCounter("Allar was das was das Allar Dicka dickA bam"))