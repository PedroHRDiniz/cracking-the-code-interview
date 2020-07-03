def isUnique(input):
  input = input.lower();
  dictionary = {};
  for character in input:
    if(character in dictionary):
      return False;
    else:
      dictionary[character] = True;
    
  return True;

def isUniqueWithoutDict(input):
  input = input.lower()
  hasUniqueCharacters = True
  for index in range(len(input)):
    currentChar = input[index]
    currentIndex = index
    for innerIndex in range(len(input)):
      if innerIndex != currentIndex:
        hasUniqueCharacters = hasUniqueCharacters and input[innerIndex] != currentChar
      if not hasUniqueCharacters:
        return False  
  return hasUniqueCharacters

#Milena Carneiro