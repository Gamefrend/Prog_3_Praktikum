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

def mostCommon(dictonary, number):
    return sorted(dictonary, key = dictonary.get, reverse=True)[:number]

if len(sys.argv) > 1:
    with open(sys.argv[1]) as inputFile:
        inputString = inputFile.read()
    print(mostCommon(charCounter(inputString),25))
    print(mostCommon(wordCounter(inputString),25))

