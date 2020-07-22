import re

def buildDictCharOccurences(string):
  characters = {}
  for index in range(len(string)):
    currentChar = string[index]
    if(currentChar not in characters):
      characters[currentChar] = 1 
    else:
      characters[currentChar] += 1

  return characters

def isPalindromePermutation(charDict):
  oddCounter = 0
  for char in charDict:
    if(charDict[char] % 2 > 0):    
      oddCounter += 1
  return oddCounter == 1  

def palindromePermutation(string):
  string = re.sub(' ','', string)
  dictFromString = buildDictCharOccurences(string)
  return isPalindromePermutation(dictFromString)

#Milena Carneiro